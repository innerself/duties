class UserButton {
  constructor(buttonId) {
    this.buttonId = buttonId;
    this.button = document.getElementById(this.buttonId);
    this.indicator = this.button.previousElementSibling;
    this.currentState = this.button.dataset.state;
    this.color = this.button.dataset.color;
  }

  turnOn() {
    this.button.dataset.state = 'on';
    this.indicator.style.backgroundColor = this.color;
  }

  turnOff() {
    this.button.dataset.state = 'off';
    this.indicator.style.backgroundColor = 'transparent';
  }

  toggle() {
    if (this.currentState === 'on') {
      this.turnOff();
    } else if (this.currentState === 'off') {
      this.turnOn();
    } else {
      console.error('Wrong state %s', this.currentState);
    }
  }
}


function toggleUserButton(buttonId) {
  const userButton = new UserButton(buttonId);
  userButton.toggle();
}
