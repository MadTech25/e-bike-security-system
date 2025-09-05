#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10
#define RELAY_PIN 3
#define BUZZER_PIN 4

MFRC522 rfid(SS_PIN, RST_PIN);

// Pre-defined UID for authorized card (replace with your card's UID)
byte authorizedUID[] = {0xDE, 0xAD, 0xBE, 0xEF};

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfid.PCD_Init();

  pinMode(RELAY_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW); // lock is off by default

  Serial.println("RFID Lock system ready.");
}

void loop() {
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial()) {
    return;
  }

  Serial.print("Card detected. UID: ");
  for (byte i = 0; i < rfid.uid.size; i++) {
    Serial.print(rfid.uid.uidByte[i], HEX);
  }
  Serial.println();

  if (isAuthorized(rfid.uid.uidByte)) {
    Serial.println("✅ Authorized access!");
    digitalWrite(RELAY_PIN, HIGH);  // Unlock
    tone(BUZZER_PIN, 1000, 200);
    delay(3000);  // Keep lock open
    digitalWrite(RELAY_PIN, LOW);   // Lock again
  } else {
    Serial.println("❌ Access denied.");
    tone(BUZZER_PIN, 500, 500);
  }

  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
}

bool isAuthorized(byte *uid) {
  for (byte i = 0; i < 4; i++) {
    if (uid[i] != authorizedUID[i]) {
      return false;
    }
  }
  return true;
}