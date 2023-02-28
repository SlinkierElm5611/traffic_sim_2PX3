from matplotlib import pyplot as plt

LEFT_TURNING_LANE: str = "left"
RIGHT_TURNING_LANE: str = "right"
NON_TURNING_LANE: str = "straight"

intersection_design: dict = {
    "roads": [
        {
            "lanes": [
                LEFT_TURNING_LANE,
                NON_TURNING_LANE,
                RIGHT_TURNING_LANE
            ]
        },
        {
            "lanes": [
                LEFT_TURNING_LANE,
                NON_TURNING_LANE,
                RIGHT_TURNING_LANE
            ]
        },
        {
            "lanes": [
                LEFT_TURNING_LANE,
                NON_TURNING_LANE,
                RIGHT_TURNING_LANE
            ]
        },
        {
            "lanes": [
                LEFT_TURNING_LANE,
                NON_TURNING_LANE,
                RIGHT_TURNING_LANE
            ]
        }
    ]
}

def simulation(intersection: dict, load: int) -> float:
    '''
    simulation code that will return the average wait time given an intersection and a load
    where we define load as the backlog of cars that are waiting to start driving (in each lane)
    '''
    total_time: int = 0
    simulation_state: list[list[dict]] = []
    number_of_lanes: int = 0
    for road in intersection.get("roads"):
        simulation_state.append(
            []
        )
        for lane in road.get("lanes"):
            simulation_state[-1].append(
                {
                    "direction": lane,
                    "load": load
                }
            )
            number_of_lanes = number_of_lanes + 1
    no_more_cars: bool = False
    direction: int = 0
    times: list[int] = []
    while(no_more_cars == False):
        if simulation_state[direction][0].get("load") > 0 or simulation_state[direction + 2][0].get("load") > 0:
            for i in range(total_time, total_time+15, 3):
                times.append(i)
            total_time = total_time + 15
            simulation_state[direction][0]["load"] = simulation_state[direction][0]["load"] - 5
            simulation_state[direction+2][0]["load"] = simulation_state[direction+2][0]["load"] - 5
        if simulation_state[direction][1].get("load") > 0 or simulation_state[direction][2].get("load") > 0 or simulation_state[direction+2][1].get("load") > 0 or simulation_state[direction+2][2].get("load") > 0:
            for i in range(total_time, total_time + 15, 3):
                times.append(i)
            total_time = total_time + 15
            for i in range(1,3):
                simulation_state[direction][i]["load"] = simulation_state[direction][i]["load"] - 5
                simulation_state[direction+2][i]["load"] = simulation_state[direction+2][i]["load"] - 5
        if direction == 1:
            direction = 0
        else:
            direction = 1
        for road in simulation_state:
            for lane in road:
                if lane["load"] < 0:
                    lane["load"] = 0
        no_more_cars = True
        for road in simulation_state:
            for lane in road:
                if lane.get("load") > 0:
                    no_more_cars =  False
    return float(sum(times)/len(times))


def main():
    '''
    Main function in simulation program
    '''
    average_wait_time: list[float] = []
    related_loads: list[int] = []
    for i in range (5, 200, 5):
        average_wait_time.append(simulation(intersection=intersection_design, load=i))
        related_loads.append(i)
    plt.plot(related_loads, average_wait_time)
    plt.show()

if __name__ == "__main__":
    main()