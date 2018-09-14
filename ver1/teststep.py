from stepper import stepper

#stepper variables
#[stepPin, directionPin, enablePin]
testStepper = stepper([35, 37, 8])

#test stepper
testStepper.step(2000, "l"); #steps, dir, speed, stayOn
