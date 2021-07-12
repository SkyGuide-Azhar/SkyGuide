#include <Wire.h>
#include <MPU6050.h>
#include <SoftwareSerial.h>

//#define HALFSTEP 4

//// Motor pin definitions
//#define RAMotor_IN1  2     // IN1 on the ULN2003 driver 1
//#define RAMotor_IN2  3     // IN2 on the ULN2003 driver 1
//#define RAMotor_IN3  4     // IN3 on the ULN2003 driver 1
//#define RAMotor_IN4  5     // IN4 on the ULN2003 driver 1
//
//#define DECMotor_IN1  6     // IN1 on the ULN2003 driver 1
//#define DECMotor_IN2  7     // IN2 on the ULN2003 driver 1
//#define DECMotor_IN3  8     // IN3 on the ULN2003 driver 1
//#define DECMotor_IN4  9     // IN4 on the ULN2003 driver 1
//
//// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48
//AccelStepper RAMotor(HALFSTEP, RAMotor_IN2, RAMotor_IN4, RAMotor_IN3, RAMotor_IN1);
//AccelStepper DECMotor(HALFSTEP, DECMotor_IN2, DECMotor_IN4, DECMotor_IN3, DECMotor_IN1);

SoftwareSerial BTSerial(3, 4); // RX | TX

MPU6050 mpu;

boolean RAStopped = false;
boolean DECStopped = false;

unsigned long timer = 0;
float timeStep = 0.01;

// Pitch and Yaw values
double pitch, yaw;

double in_DEC, in_RA;  //variable to store the user input DEC and RA

const int stahp=7,stahp2=10;
const int cw=6,cw2=9;
const int ccw=8,ccw2=11;

void setup() 
{
    Serial.begin(115200);
    BTSerial.begin(9600);

     pinMode(stahp,OUTPUT);
    pinMode(cw,OUTPUT);
    pinMode(ccw,OUTPUT);
    pinMode(stahp2,OUTPUT);
    pinMode(cw2,OUTPUT);
    pinMode(ccw2,OUTPUT);
  
    //delay(5000);  //wait before starting
    
    while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
    {
    Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
    delay(500);
    }
    mpu.calibrateGyro();
    mpu.setThreshold(3);
}

void loop()
{   
      
    recvdata();

    timer = millis();
    Vector norm = mpu.readNormalizeGyro();
  
    //I've put the sensor with a 90 degree angle on the setup due to
    //cable connection problems. Because of that the data values from the mpu6050 chip are
    //different in this case:
    //roll data(X-axis) is pitch.
    //pitch data(Y-axis) is yaw.

    yaw = yaw + norm.YAxis * timeStep;
    pitch = pitch + norm.XAxis * timeStep;
 
    Serial.print(" Yaw = ");
    Serial.print(yaw);
    Serial.print(" Pitch = ");
    Serial.println(pitch);

    DecCheck();
    RACheck();

    
    Serial.print(" RA = ");
    Serial.print(in_RA);
    Serial.print(" DEC = ");
    Serial.println(in_DEC);

//    if(RAStopped==false)
        
//        
//    if(DECStopped==false)
//        DECMotor.run();

    //Serial.println((timeStep*1000) - (millis() - timer));
    delay(abs((timeStep*1000) - (millis() - timer)));//timer for the gyro. 
}


void recvdata()
{
  //This function receives data from serial as (0.00,0.00)
  //splits it to strings by the comma ","
  //then converts them to doubles 
    Serial.println(BTSerial.available());
    if (BTSerial.available())
    {
        String UserInput = BTSerial.readString();
        String UserRA, UserDec;

        Serial.println(UserInput);
    
        for (int i = 0; i < UserInput.length(); i++) 
        {
            if (UserInput.substring(i, i+1) == ",") 
            {
                UserRA = UserInput.substring(0, i);
                UserDec= UserInput.substring(i+1);
                break;
            }
        }
    
        in_DEC = 90 - UserDec.toFloat(); // "90 - " cuz the pitch's zero is 90(polaris)
        in_RA  = UserRA.toFloat();

        BTSerial.println("1");
    }
}


void DecCheck() // DEC
{ 

    if(floor(pitch*100) == floor(in_DEC*100))
    {
        digitalWrite(stahp2,HIGH);
        }else{
        digitalWrite(stahp2,LOW);
    }
    if(floor(pitch*100) < floor(in_DEC*100)){
        digitalWrite(cw2,HIGH);
        }else{
        digitalWrite(cw2,LOW);
    }
    if(floor(pitch*100) > floor(in_DEC*100)){
        digitalWrite(ccw2,HIGH);
        }else{
        digitalWrite(ccw2,LOW);
        }
}


void RACheck() // RA
{ 


    if(floor(yaw*100) == floor(in_RA*100))
    {
        digitalWrite(stahp,HIGH);
        }else{
        digitalWrite(stahp,LOW);
    }
    if(floor(yaw*100) < floor(in_RA*100)){
        digitalWrite(cw,HIGH);
        }else{
        digitalWrite(cw,LOW);
    }
    if(floor(yaw*100) > floor(in_RA*100)){
        digitalWrite(ccw,HIGH);
        }else{
        digitalWrite(ccw,LOW);
        }
}
