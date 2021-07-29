class UserButton {
  constructor(username) {
    this.username = username;
    this.buttonId = 'button-'.concat(this.username);
    this.button = document.getElementById(this.buttonId);
    this.indicator = this.button.previousElementSibling;
    this.currentState = this.button.dataset.state;
    this.color = this.button.dataset.color;
  }

  turnOn() {
    this.button.dataset.state = 'on';
    this.indicator.style.backgroundColor = this.color;
    fetch('http://127.0.0.1:8000/get/duties/'.concat(this.username).concat('/'))
      .then(response => response.json())
      .then(data => this.highlight_calendar(data));
  }

  turnOff() {
    this.button.dataset.state = 'off';
    this.indicator.style.backgroundColor = 'transparent';
    fetch('http://127.0.0.1:8000/get/duties/'.concat(this.username).concat('/'))
      .then(response => response.json())
      .then(data => this.clear_calendar(data));
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

  highlight_calendar(dutyDates) {
    for (const dutyDate of dutyDates) {
      const dateObj = document.getElementById(dutyDate);
      dateObj.style.backgroundColor = this.color;
      dateObj.classList.toggle('highlighted')
    }
  }

  clear_calendar(dutyDates) {
    for (const dutyDate of dutyDates) {
      const dateObj = document.getElementById(dutyDate);
      dateObj.style.backgroundColor = 'transparent';
      dateObj.classList.toggle('highlighted')
    }
  }

  // fetch_duty_dates() {
  //   var duties;
  //
  //   fetch('http://127.0.0.1:8000/get/duties/<here-is-username>/')
  //     .then(response => response.json())
  //     .then(data => duties = data);
  //
  //   return duties
  // }
}


function toggleUserButton(username) {
  const userButton = new UserButton(username);
  userButton.toggle();
}
