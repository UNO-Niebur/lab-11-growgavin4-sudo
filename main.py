# StopLightSim.py
# Name:Gavin Grow
# Date:4/17/26
# Assignment:create a simulation 

import simpy

# Global variable to track light state
greenLight = True


def stopLight(env):
    """Simulates a traffic light that cycles between green, yellow, and red."""
    global greenLight

    while True:
        print("Green")
        greenLight = True
        yield env.timeout(30)

        print("Yellow")
        yield env.timeout(2)

        print("Red")
        greenLight = False
        yield env.timeout(20)


def car(env, car_id):
    """Simulates a car arriving and waiting for the light."""
    
    print("Car", car_id, ": Arrived at", env.now)

    # Make the car wait while the light is red
    while not greenLight:
        yield env.timeout(1)

    print("Car", car_id, ": Departed at", env.now)


def carArrival(env):
    """Creates cars at regular intervals."""
    
    car_id = 0

    while True:
        car_id += 1

        # Start a new car process
        env.process(car(env, car_id))

        yield env.timeout(5)


def main():
    env = simpy.Environment()

    # Start processes
    env.process(stopLight(env))
    env.process(carArrival(env))

    # Run simulation
    env.run(until=100)

    print("Simulation complete")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
