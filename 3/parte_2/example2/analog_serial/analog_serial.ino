// Read analog values from A0 and print them to serial port.


void setup() {
  // initialize serial comms
  Serial.begin(9600); 
}

void loop() {
  // read A0
  float data = analogRead(A0);
  data = (data/1024.00) * 5;
  String dataToSend = String(data);
  Serial.println(dataToSend);
  // wait 
  delay(300);  
}
