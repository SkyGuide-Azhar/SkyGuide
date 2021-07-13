#include <AccelStepper.h>
#include <Wire.h>

#define HALFSTEP 8

#define motorPin1  2      // IN1 on the ULN2003 driver 1 (RA)
#define motorPin2  3      // IN2 on the ULN2003 driver 1 (RA)
#define motorPin3  4      // IN3 on the ULN2003 driver 1 (RA)
#define motorPin4  5      // IN4 on the ULN2003 driver 1 (RA)

#define motorPin5  A0     // IN1 on the ULN2003 driver 2 (DEC)
#define motorPin6  A1     // IN2 on the ULN2003 driver 2 (DEC)
#define motorPin7  A2     // IN3 on the ULN2003 driver 2 (DEC)
#define motorPin8  A3     // IN4 on the ULN2003 driver 2 (DEC)

#define RA_Stop  7        // Master RA stop control signal
#define RA_CW    6        // Master RA CW control signal
#define RA_CCW   8        // Master RA CCW control signal

#define DEC_Stop 10       // Master DEC stop control signal
#define DEC_CW   9        // Master DEC CW control signal
#define DEC_CCW  11       // Master DEC CCW control signal

AccelStepper RA_Stepper  (HALFSTEP, motorPin2, motorPin4, motorPin3, motorPin1);
AccelStepper DEC_Stepper (HALFSTEP, motorPin6, motorPin8, motorPin7, motorPin5);


boolean RA_Stopped = false;
boolean DEC_Stopped = false;

void setup() 
{
    RA_Stepper.setMaxSpeed(1000.0);
    DEC_Stepper.setMaxSpeed(1000.0);
	
    pinMode(DEC_Stop,INPUT);
    pinMode(DEC_CW,INPUT);
    pinMode(DEC_CCW,INPUT);
	
    pinMode(RA_Stop,INPUT);
    pinMode(RA_CW,INPUT);
    pinMode(RA_CCW,INPUT);
}

void loop()
{
    DEC_MotorUpdate();
    RA_MotorUpdate();
    
    if(RA_Stopped==false)
        RA_Stepper.run();
    
    if(DEC_Stopped==false)
        DEC_Stepper.run();
    
}


void RA_MotorUpdate()
{
    if(digitalRead(RA_Stop)==HIGH)
        RA_Stopped = true;
    else if(digitalRead(RA_CW)==HIGH)
	{
        RA_Stepper.setSpeed(500);
        RA_Stopped = false;
    }
	else if(digitalRead(RA_CCW)==HIGH)
	{
        RA_Stepper.setSpeed(-500);
        RA_Stopped = false;
    }
}


void DEC_MotorUpdate()
{
    if(digitalRead(DEC_Stop)==HIGH)
        DEC_Stopped = true;
    else if(digitalRead(DEC_CW)==HIGH)
	{
        DEC_Stepper.setSpeed(500);
        DEC_Stopped = false;
    }
    else if(digitalRead(DEC_CCW)==HIGH)
	{
        DEC_Stepper.setSpeed(-500);
        DEC_Stopped = false;
    }  
}