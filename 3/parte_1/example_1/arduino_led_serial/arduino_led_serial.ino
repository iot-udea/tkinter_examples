/* Simple Serial ECHO script : Written by ScottC 03/07/2012 */
/* Use a variable called byteRead to temporarily store
the data coming from the computer */

byte byteRead;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  // Turn the Serial Protocol ON
  Serial.begin(9600);
  
}


void loop() {
  /* check if data has been sent from the computer: */
  if (Serial.available()) {
    /* read the most recent byte */
    byteRead = Serial.read();
    if(byteRead == 'h') {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if(byteRead == 'l') {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
