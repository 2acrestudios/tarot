## Tarot Reading with Ollama: A Python-Powered Mystic Guide

<img src="https://2acrestudios.com/wp-content/uploads/2024/05/00034-2625303745.png" align="right" style="width:300px;" />

This repository houses a Python script that leverages the power of Ollama, a large language model, to provide insightful and interactive tarot readings. 

**Key Features:**

* **Ollama Integration:** The script interacts with a local Ollama server to generate tarot card interpretations based on user prompts and selected spreads. 
* **Multiple Spreads:** Choose from various tarot spreads, including the classic Celtic Cross, Three-Card Spread, Past/Present/Future, and more. 
* **Customizable Readings:** Select the number of cards for your reading and specify the topic or question you want to explore. 
* **Detailed Interpretations:** Ollama provides rich and insightful interpretations of the drawn cards, offering guidance and clarity.
* **ASCII Art Visualization:**  The reading experience is enhanced with ASCII art representations of the tarot cards.

**Requirements:**

* **Python 3.x:** Ensure you have Python 3 installed on your system.
* **Required Libraries:** Install the necessary libraries using pip:
    ```bash
    pip install requests termcolor
    ```
* **Ollama Server:** Set up a local Ollama server and ensure it's running. You can find instructions for setting up Ollama in its official documentation.

**Instructions:**

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/tarot-ollama.git
    ```

2. **Configure Ollama Settings:**
    * Open `tarot.py` and modify the `OLLAMA_API_URL` and `OLLAMA_MODEL_NAME` variables to match your Ollama server's URL and the desired language model.

3. **Run the Script:**
    ```bash
    python tarot.py 
    ```
    * Follow the prompts to select your desired topic, choose a tarot spread, and specify the number of cards (if applicable).
    * The script will display the generated tarot reading, along with optional ASCII art representations of the cards.

**Customization:**

* **Tarot Spreads:** You can easily add more tarot spreads to the `tarot_spreads` list in `tarot.py`.  Define the number of cards for each spread in the `spread_card_count` dictionary.
* **Card Interpretations:** The prompt in `tarot.py` guides Ollama's interpretation style. Modify the prompt to adjust the tone, level of detail, or specific instructions for different spreads.
* **ASCII Art:** The `tarot_cards_ascii.py` file contains ASCII art for a selection of tarot cards. You can add more cards or customize the existing art as desired.

**Additional Notes:**

* The accuracy and quality of the tarot readings depend on the capabilities of the Ollama language model you use. Experiment with different models to find one that resonates with your preferences.
* This script is for entertainment and personal exploration purposes.  Tarot readings should not be considered a substitute for professional advice or guidance.

**Enjoy your journey into the mystical world of tarot with the power of Ollama!**
