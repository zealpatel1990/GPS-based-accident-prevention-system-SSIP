from stepper import stepper

#stepper variables
#[stepPin, directionPin, enablePin]
testStepper = stepper([22, 17, 23])

#test stepper
testStepper.step(3200, "right"); #steps, dir, speed, stayOn