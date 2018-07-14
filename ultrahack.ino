// connect motor controller pins to Arduino digital pins
// motor one
int enA = 10;
int in1 = 8;
int in2 = 9;

#include <Servo.h>
 Servo Servo1;
 int servoPin = 4;  

void setup()
{
  Serial.begin(9600); 
Servo1.attach(servoPin);  
  // set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
   pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
 }
void demoOne()
{
  
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  // set speed to 200 out of possible range 0~255
  analogWrite(enA, 255);
  }
 void loop()
{
    int inByte;
if(Serial.available()){
   inByte=Serial.read();
   if(inByte==1){
   Servo1.write(60); 
   delay(1000);
   }

}
Servo1.write(0);
if(Serial.available()){
   if(inByte==0){
    Servo1.write(-60);
    delay(1000);
    }
   }
  demoOne();
  delay(2000);
 
}
