# AI_Assignment_2

This assignment is for the MAY-AUG trimester.

# Note: This code is a simplified example of an expert system for a restaurant.

In a real-world application, you would likely use a more complex structure and possibly a database.
This example is meant to illustrate the basic concepts of frames and production rules in an expert system.
The allergy check and dish recommendations are basic and would need to be expanded for a full application.
Additionally, error handling and user input validation would be necessary for robustness.

# 🍽️ AI Restaurant Expert System

## Overview

The **AI Restaurant Expert System** is a rule-based knowledge representation prototype developed in Python. It simulates a smart restaurant assistant capable of:

- Recommending safe dishes for customers based on their allergies.
- Suggesting daily specials dynamically based on the time of day and customer type.
- Applying rule-based reasoning to guide decision-making.

This system is a practical application of artificial intelligence principles including **frames**, **production rules**, and a basic **inference engine**, tailored to the restaurant domain.

---

## Features

✅ Customer allergy detection and dish filtering  
✅ Context-aware meal suggestions  
✅ Modular, extensible codebase with clearly defined knowledge structures  
✅ Demonstrates declarative, procedural, and heuristic knowledge application

---

## Technologies Used

- **Python 3.x**
- Procedural logic and rule-based decision making
- AI concepts from "Knowledge Representation" and "Problem Solving in AI"

---

## System Components

### 1. Knowledge Base (Frames)

- **Menu items** are represented using dictionaries (frames) with fields such as `ingredients`, `price`, and `type`.
- **Customers** are represented by dictionaries including their name, allergy list, and customer type.

### 2. Rule Engine (Production Rules)

Implements expert rules such as:

- If a customer is allergic to an ingredient in a dish → do not recommend it.
- If it's lunch and the customer is new → suggest the daily special.

### 3. Inference Engine

- Applies the rules to the knowledge base
- Filters and recommends safe dishes
- Prints reasoning and decision-making transparently to the console

---

## How It Works

1. The system defines the **menu** and **customer data**.
2. It evaluates the **current time** to determine which suggestions apply.
3. The inference engine checks all dishes against customer allergies.
4. Only safe and appropriate dishes are recommended.

---

## Sample Output

        CHECK "Output.png" file to view the sample output.

---

## Use Cases

- Smart restaurant recommendation systems.
- Food delivery assistant chatbots.
- Allergy-sensitive menu filtering.
- Teaching and demonstrating AI reasoning concepts in academic settings.

---

## Future Enhancements

- Integration with a real-time reservation and ordering system.
- Natural language input via NLP models.
- Support for fuzzy reasoning and probabilistic decision-making.
- Web-based GUI or chatbot frontend.

---

## License

This project is intended for educational and demonstration purposes. No warranties are expressed or implied.

---

## Author

Developed as part of a knowledge representation module on **Artificial Intelligence** by Etemesi.
