## Blackjack 🃏

A simple command-line implementation of the classic **Blackjack** card game written in Python.
The player competes against the computer dealer, aiming to score as close to 21 as possible without going over.

---

## 📜 Features

* **Random Card Dealing** – Simulates drawing cards from a deck.
* **Blackjack Detection** – Recognizes natural Blackjack (Ace + 10-value card).
* **Ace Adjustment** – Automatically changes Ace from 11 to 1 to prevent busting.
* **Computer Dealer AI** – Dealer draws until reaching at least 17.
* **Interactive Gameplay** – Players can choose to draw another card or pass.
* **Winner Determination** – Clear messages for win, loss, and draw situations.


## 🎮 How to Play

1. You and the dealer (computer) are each dealt two cards.
2. The goal is to get a hand value as close to **21** as possible without exceeding it.
3. Number cards are worth their face value, face cards (J, Q, K) are worth 10, and Aces are worth 11 or 1 depending on the situation.
4. You can choose to:

   * **Hit (Y)** – Draw another card.
   * **Stand (N)** – Keep your current hand.
5. The dealer draws cards until the score is **17 or more**.
6. The results are compared and the winner is declared.

---

## 🏆 Scoring Rules

* **Blackjack (Ace + 10-value card)**: Automatically wins unless the dealer also has Blackjack.
* **Over 21**: Bust – automatic loss.
* **Closer to 21 than opponent**: Wins.
* **Tie**: Draw.