//Motion_Template provides a framework for controlling robot using python
//Get commands from python Serial.write("Command")
//Commands should use this system:
//First character C - Command or M - Motor Possition
//For M 
//Second and Third Characters designate which motor: 01 - 16
//4th - 6th characters designate degree turn: 001 - 360
//For C
//Second and Third Characters designate movement sequence
//SL = Salute
//Additional rules can be added here

#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
#define DXL_BUS_SERIAL2 2  //Dynamixel on Serial2(USART2)  <-LN101,BT210
#define DXL_BUS_SERIAL3 3  //Dynamixel on Serial3(USART3)  <-OpenCM 485EXP

#define ShoulderR 2
#define ShoulderL 1
#define ArmR 3
#define ArmL 4
#define WristR 5
#define WristL 6
#define HipR 7
#define HipL 8
#define ThighR 9
#define ThighL 10
#define KneeR 11
#define KneeL 12
#define LegR 13 
#define LegL 14
#define FootR 15
#define FootL 16

int offSL = 15;
int offSR = 15;
int offAL = 15;
int offAR = 0;
int offWL = 0;
int offWR = 0;
int offHL = 5;
int offHR = 0;
int offTL = 20;
int offTR = 15;
int offKL = 25;
int offKR = 15;
int offLL = 0;
int offLR = 25;
int offFL = 0;
int offFR = 15;

int q1 = 185; //1st quarter turn (q1 = 90 degrees Minimum)
int c1 = 355; //1.5 quarter turn (c1 = 135 degrees)
int q2 = 500; //2nd quarter turn (q2 = 180 degrees)
int c3 = 655; //2.5 quarter turn (c3 = 225 degrees)
int q3 = 825; //3rd quarter turn (q3 = 270 degrees Maximum)

int ErrorChar = 'a';
int ErrorValue = 0;

Dynamixel Dxl(DXL_BUS_SERIAL1); //Leave set to Serial1

void setup() {
  
  pinMode(BOARD_LED_PIN, OUTPUT);
  Dxl.begin(3);  
  Dxl.jointMode(ShoulderR); 
  Dxl.jointMode(ShoulderL); 
  Dxl.jointMode(ArmR); 
  Dxl.jointMode(ArmL); 
  Dxl.jointMode(WristR); 
  Dxl.jointMode(WristL); 
  Dxl.jointMode(HipL); 
  Dxl.jointMode(HipR); 
  Dxl.jointMode(ThighL); 
  Dxl.jointMode(ThighR); 
  Dxl.jointMode(KneeL); 
  Dxl.jointMode(KneeR); 
  Dxl.jointMode(LegL); 
  Dxl.jointMode(LegR); 
  Dxl.jointMode(FootL); 
  Dxl.jointMode(FootR); 
  
  SerialUSB.attachInterrupt(usbInterrupt);

  
  initialPosition();  //Set all motors to standard, standing position (q2 + natural offset)
  delay(1000);
}


void usbInterrupt(byte* buffer, byte nCount){
  char comString[] = "";
  int length = SerialUSB.available();
  while(SerialUSB.available() > 0){
    int inChar = SerialUSB.read();
    comString[length - SerialUSB.available()-1] += (char)inChar;
  }
  
  if(length > 0){ 
    
    if(comString[0] == 'M' && length == 6){
      
      int m1 = comString[1] - '0';
      int m2 = comString[2] - '0';
      int motor = m1*10 + m2;
      
      int d1 = comString[3] - '0';
      int d2 = comString[4] - '0';
      int d3 = comString[5] - '0';
      int degree = ((d1*100 + d2*10 + d3));
      ErrorValue = degree;
      
      if(degree<90){
        degree = 90;
      }
      if(degree>270){
        degree = 270;
      }
      
      if(motor % 2 == 0){
         degree = 180 - (degree - 180);
      }
      
      degree = (((degree-90)*630)/180)+185;
      
      Dxl.goalPosition(motor, degree); 
    }
      
    
    if(comString[0] == 'C' && length == 3){
      
      if(comString[1] == 'I' && comString[2] == 'N'){
        initialPosition();
        delay(500);
      }
      
      if(comString[1] == 'S' && comString[2] == 'L'){ //Salute
        salute();
        delay(1500);
        initialPosition();
        delay(500);
        attention();
        delay(500);
        initialPosition();
        }
     }
  }
}

void initialPosition(){
 Dxl.goalPosition(ShoulderR, q2 + offSR); 
 Dxl.goalPosition(ShoulderL, q2 + offSL);
 Dxl.goalPosition(ArmR, q2 + offAR); 
 Dxl.goalPosition(ArmL, q2 + offAL);
 Dxl.goalPosition(WristR, q2 + offWR); 
 Dxl.goalPosition(WristL, q2 + offWL);
 Dxl.goalPosition(HipR, q2 + offHR); 
 Dxl.goalPosition(HipL, q2 + offHL);
 Dxl.goalPosition(ThighR, q2 + offTR); 
 Dxl.goalPosition(ThighL, q2 + offTL);
 Dxl.goalPosition(KneeR, q2 + offKR); 
 Dxl.goalPosition(KneeL, q2 + offKL);
 Dxl.goalPosition(LegR, q2 + offLR); 
 Dxl.goalPosition(LegL, q2 + offLL);
 Dxl.goalPosition(FootR, q2 + offFR); 
 Dxl.goalPosition(FootL, q2 + offFL);
}

void loop() {
  SerialUSB.print(ErrorChar);
  SerialUSB.print(' ');
  SerialUSB.println(ErrorValue);
  delay(1000);
}


void attention(){
 delay(500);
 Dxl.goalPosition(ArmR, q3); 
 Dxl.goalPosition(ArmL, q1);
 delay(500);
}


void salute(){
  attention();
  delay(500);
  Dxl.goalPosition(ShoulderR, 950);
  Dxl.goalPosition(ArmR, 750);
  delay(500);
  Dxl.goalPosition(WristR, q3);
  delay(2000);
}
