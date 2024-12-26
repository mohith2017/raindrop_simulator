import random

'''
RainDrop -
    generate_raindrop()
    fill(sidewalk, raindrop)

SideWalk -
    __init__()
    is_fully_wet()
    simulate()
'''
class Drop:
    def __init__(self, type):
        if type == "same":
            self.type = type
            self.x = -1

        elif type == "split":
            self.type = type
            self.x1 = -1
            self.y1 = -1
            self.section1 = 0

            self.x2 = -1
            self.y2 = -1
            self.section2 = 0


class RainDrop:
    def generate_raindrop(self):
        # Generate 1 raindrop
        type = random.choice(["same" , "split"])
        new_drop = Drop(type)
        if type == "same":
            new_drop.x = random.randint(0, 99)


        else:
            new_drop.x1  = random.randint(1, 98)
            new_drop.y1 = random.choice([0, 1])

            if new_drop.y1 == 0:
                new_drop.x2 = new_drop.x1 + 1
                new_drop.y2 = 1

            else:
                new_drop.x2 = new_drop.x1 - 1
                new_drop.y2 = 0

            new_drop.section1 = random.random() * 0.5
            new_drop.section2 = random.random() * 0.5

        return new_drop

    def fill(self, sidewalk, raindrop: Drop):
        # Fill the 1 raindrop
        if raindrop.type == "same":
            sidewalk[raindrop.x][0] = 0.5
            sidewalk[raindrop.x][1] = 0.5

        else:
            if (sidewalk[raindrop.x1][raindrop.y1] + raindrop.section1) <= 0.5:
                sidewalk[raindrop.x1][raindrop.y1] += raindrop.section1
            if (sidewalk[raindrop.x2][raindrop.y2] + raindrop.section2) <= 0.5:
                sidewalk[raindrop.x2][raindrop.y2] += raindrop.section2


class SideWalk:
    def __init__(self):
        self.sidewalk = [[0,0] for _ in range(100)]

    def is_fully_wet(self):
        for i in range(len(self.sidewalk)):
            for j in range(2):
                if self.sidewalk[i][j] != 0.5:
                    return False
                
        return True

    def simulate(self, no_trials):
        # Function to fill the sidewalk & calculate the avg number of raindrops
        print("Beginning Simulation...")
        raindrop_obj = RainDrop()
        total_drops = 0
        print("Total Number of trials: ", no_trials)
        
        for i in range(no_trials):
            drop_count = 0
            self.sidewalk = [[0,0] for _ in range(100)]
            
            while not self.is_fully_wet():
                raindrop = raindrop_obj.generate_raindrop()
                raindrop_obj.fill(self.sidewalk, raindrop)
                drop_count += 1

            total_drops += drop_count
            print("Drop_count in Iteration ", i+1, ":", drop_count)

        return (total_drops / no_trials)
            

        
    
if __name__ == "__main__":
    # Change the number of trials to any number of times you'd like to run the simulation
    # (I've chosen a random number between 10 & 99 for simplicity)
    sidewalk = SideWalk()
    no_trials = random.randint(10, 99)
    avg = sidewalk.simulate(no_trials)
    print("Number of raindrops that are required to fill the sidewalk on average: ", avg)
