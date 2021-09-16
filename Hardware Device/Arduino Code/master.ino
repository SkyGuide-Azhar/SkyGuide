#include <Wire.h>
#include <MPU6050.h>
#include <SoftwareSerial.h>

#define RA_Stop  7
#define RA_CW    6
#define RA_CCW   8

#define DEC_Stop 10
#define DEC_CW   9
#define DEC_CCW  11


SoftwareSerial BTSerial(3, 4); // RX , TX

MPU6050 mpu;

boolean RAStopped = false;
boolean DECStopped = false;

unsigned long timer = 0;
float timeStep = 0.01;


double pitch, roll;

double in_DEC, in_RA;  //variable to store the user input DEC and RA

void setup() 
{
    Serial.begin(115200);
    BTSerial.begin(9600);

    pinMode(RA_Stop,OUTPUT);
    pinMode(RA_CW,OUTPUT);
    pinMode(RA_CCW,OUTPUT);
    pinMode(DEC_Stop,OUTPUT);
    pinMode(DEC_CW,OUTPUT);
    pinMode(DEC_CCW,OUTPUT);
    
    while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))delay(500);
	
    mpu.calibrateGyro();
    mpu.setThreshold(3);
}

void loop()
{   
      
    recvdata();

    timer = millis();
    Vector norm = mpu.readNormalizeGyro();
  

    roll  = roll + norm.YAxis * timeStep;
    pitch = pitch + norm.XAxis * timeStep;
 
    Serial.print(" roll = ");
    Serial.print(roll);
    Serial.print(" Pitch = ");
    Serial.println(pitch);

    DecCheck();
    RACheck();

    
    Serial.print(" RA = ");
    Serial.print(in_RA);
    Serial.print(" DEC = ");
    Serial.println(in_DEC);

    delay(abs((timeStep*1000) - (millis() - timer)));//timer for the gyro. 
}


void recvdata()
{ 
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


void DecCheck()
{ 

    if(floor(pitch) == floor(in_DEC))
        digitalWrite(DEC_Stop,HIGH);
    else
        digitalWrite(DEC_Stop,LOW);
    
    if(floor(pitch) < floor(in_DEC))
        digitalWrite(DEC_CW,HIGH);
    else
        digitalWrite(DEC_CW,LOW);
    
    if(floor(pitch) > floor(in_DEC))
        digitalWrite(DEC_CCW,HIGH);
    else
        digitalWrite(DEC_CCW,LOW);
        
}


void RACheck()
{ 

    if(floor(roll) == floor(in_RA))
        digitalWrite(RA_Stop,HIGH);
	else
        digitalWrite(RA_Stop,LOW);

    if(floor(roll) < floor(in_RA))
        digitalWrite(RA_CW,HIGH);
	else
        digitalWrite(RA_CW,LOW);
	
    if(floor(roll) > floor(in_RA))
        digitalWrite(RA_CCW,HIGH);
	else
        digitalWrite(RA_CCW,LOW);
}