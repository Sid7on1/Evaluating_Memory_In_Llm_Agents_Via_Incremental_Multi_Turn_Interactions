import random

class LLMAgent:
    """
    A simplified LLM agent that simulates memory through a list of interactions.
    This agent evaluates memory by tracking its ability to recall past interactions
    in multi-turn conversations.
    """

    def __init__(self, initial_state=""):
        """
        Initializes the agent with an empty memory (interaction history) and an optional initial state.
        """
        self.memory = []  # List to store past interactions (tuples of (user_input, agent_response))
        self.current_state = initial_state

    def respond(self, user_input):
        """
        Generates a response based on the user input and the agent's memory.
        This is a simplified simulation; a real LLM would use a more complex model.
        """

        # Simulate memory recall by considering past interactions
        context = "\n".join([f"User: {u}\nAgent: {a}" for u, a in self.memory])

        # Simulate response generation based on input and context
        response = self._generate_response(user_input, context, self.current_state)

        # Update memory with the current interaction
        self.memory.append((user_input, response))

        return response

    def _generate_response(self, user_input, context, current_state):
        """
        A very basic response generator.  In a real LLM, this would be a complex model.
        This version just echoes back the user input with some modifications based on context.
        """
        if "remember" in user_input.lower():
            # Attempt to recall something from memory
            if self.memory:
                last_interaction = self.memory[-1]
                return f"I remember you said: {last_interaction[0]}, and I replied: {last_interaction[1]}"
            else:
                return "I don't remember anything yet."
        elif "state" in user_input.lower():
            return f"My current state is: {self.current_state}"
        else:
            # Echo back the input with a slight modification
            possible_responses = [
                f"You said: {user_input}",
                f"I heard you say: {user_input}",
                f"So, you're saying: {user_input}"
            ]
            return random.choice(possible_responses)

    def clear_memory(self):
        """
        Clears the agent's memory.
        """
        self.memory = []

# Example usage:
if __name__ == '__main__':
    agent = LLMAgent(initial_state="Ready to chat.")

    print(agent.respond("Hello!"))
    print(agent.respond("What is your state?"))
    print(agent.respond("Remember what I just said?"))
    print(agent.respond("Clear your memory"))
    print(agent.respond("Remember what I just said?"))