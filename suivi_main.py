import cv2
import mediapipe as mp
from pythonosc import udp_client

# Initialisation de MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Configuration du client OSC
ip = "127.0.0.1"  # Adresse IP de la machine (localhost)
port = 8000       # Port de réception dans TouchDesigner
client = udp_client.SimpleUDPClient(ip, port)

# Fonction pour déterminer à quel point la main est fermée (valeur de 0 à 1)
def get_hand_closed_value(hand_landmarks):
    # Calcule la différence moyenne des positions Y des bouts des doigts par rapport à leurs MCP (articulations principales)
    finger_tips = [
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    ]
    finger_mcps = [
        hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
        hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
        hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
        hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
    ]

    # Vérifie combien de doigts sont pliés (plus bas que leur MCP)
    closed_fingers = sum(1 for tip, mcp in zip(finger_tips, finger_mcps) if tip.y > mcp.y)
    return closed_fingers / 4  # Retourne une valeur entre 0 (ouverte) et 1 (fermée)

# Capture vidéo depuis la webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Erreur lors de la capture vidéo")
        break

    # Conversion de l'image en RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Traitement de l'image pour détecter les mains
    results = hands.process(image_rgb)

    # Dessin des annotations sur l'image
    if results.multi_hand_landmarks and results.multi_handedness:
        for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Identification de la main (Droite ou Gauche)
            hand_label = hand_info.classification[0].label
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

            # Correction de l'inversion des mains
            if hand_label == "Left":
                hand_label = "Right"
            elif hand_label == "Right":
                hand_label = "Left"

            # Calcul de la valeur de fermeture de la main
            closed_value = get_hand_closed_value(hand_landmarks)

            # Envoi des données via OSC
            client.send_message(f"/{hand_label.lower()}_hand/position_x", wrist.x)
            client.send_message(f"/{hand_label.lower()}_hand/position_y", wrist.y)
            client.send_message(f"/{hand_label.lower()}_hand/closed_value", closed_value)

    # Affichage de l'image
    cv2.imshow('Suivi des mains', image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()