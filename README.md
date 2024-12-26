### About the Project

This project simulates the process of raindrops falling on a sidewalk to determine the average number of raindrops required to fully wet the sidewalk. It utilizes a combination of random number generation and conditional logic to mimic the behavior of raindrops falling and accumulating on the sidewalk.

### Functions and their descriptions

* `generate_raindrop()`: Generates a single raindrop with a random type (either "same" or "split") and assigns properties based on the type.
* `fill(sidewalk, raindrop)`: Simulates the effect of a raindrop on the sidewalk, updating the sidewalk's wetness levels accordingly.
* `is_fully_wet()`: Checks if the entire sidewalk is fully wet, returning `True` if all sections are at maximum wetness and `False` otherwise.
* `simulate(no_trials)`: Runs multiple simulations to calculate the average number of raindrops required to fully wet the sidewalk.


### How to Run Locally

1. Clone the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required libraries by running `pip install -r requirements.txt` in your terminal/command prompt.
4. Navigate to the project directory and run `python assessment.py` to execute the simulation.

### Sample Output
Here's a sample image of the output from this function -

![Sample Output](https://i.ibb.co/9hzJ8fb/Screen-Shot-2024-12-26-at-12-31-02-PM.png)
