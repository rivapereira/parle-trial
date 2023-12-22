{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN1GVbE84w+yCvPh+lifHY5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rivapereira/parle-trial/blob/main/Trial_of_ParlAI.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "id": "4e77y8KeSwHI"
      },
      "outputs": [],
      "source": [
        "# Install ParlAI\n",
        "!pip install parlai==1.7.2\n",
        "\n",
        "# Import necessary modules\n",
        "from parlai.core.agents import Agent\n",
        "from parlai.core.params import ParlaiParser\n",
        "from parlai.core.worlds import create_task\n",
        "\n",
        "# Define a custom agent class named RepeatLabelAgent that inherits from the Agent class\n",
        "class RepeatLabelAgent(Agent):\n",
        "    # Initialize the agent by setting its id\n",
        "    def __init__(self, opt):\n",
        "        self.id = 'RepeatLabel'\n",
        "\n",
        "    # Store the observation for later and return it unmodified\n",
        "    def observe(self, observation):\n",
        "        self.observation = observation\n",
        "        return observation\n",
        "\n",
        "    # Return a reply where the text is the observed labels or \"I don't know.\"\n",
        "    def act(self):\n",
        "        reply = {'id': self.id}\n",
        "        if 'labels' in self.observation:\n",
        "            reply['text'] = ', '.join(self.observation['labels'])\n",
        "        else:\n",
        "            reply['text'] = \"I don't know.\"\n",
        "        return reply\n",
        "\n",
        "# Create a ParlaiParser object to parse command-line arguments\n",
        "parser = ParlaiParser()\n",
        "opt = parser.parse_args()\n",
        "\n",
        "# Create an instance of the RepeatLabelAgent class using the parsed options\n",
        "agent = RepeatLabelAgent(opt)\n",
        "\n",
        "# Create a world with the specified task and agent\n",
        "world = create_task(opt, agent)\n",
        "\n",
        "# Simulate a conversation for 10 rounds\n",
        "for _ in range(10):\n",
        "    # Perform a single turn in the conversation\n",
        "    world.parley()\n",
        "\n",
        "    # Display the current state of the world (conversation)\n",
        "    print(world.display())\n",
        "\n",
        "    # Check if the epoch (conversation) is done\n",
        "    if world.epoch_done():\n",
        "        print('EPOCH DONE')\n",
        "        break\n"
      ]
    }
  ]
}

