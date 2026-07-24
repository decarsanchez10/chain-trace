#include <Arduino.h>
#include "rfid_reader.h"
#include "rtc_module.h"
#include "motion_sensor.h"
#include "tamper_sensor.h"
#include "hash_builder.h"
#include "wifi_upload.h"

void setup() {
    Serial.begin(115200);
    Serial.println("ChainTrace ESP32 Initializing...");
}

void loop() {
    // Main loop logic
    delay(1000);
}
