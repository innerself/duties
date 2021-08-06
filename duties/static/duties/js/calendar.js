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
      .then(data => this.highlightCalendar(data));
  }

  turnOff() {
    this.button.dataset.state = 'off';
    this.indicator.style.backgroundColor = 'transparent';
    fetch('http://127.0.0.1:8000/get/duties/'.concat(this.username).concat('/'))
      .then(response => response.json())
      .then(data => this.clearCalendar(data));
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

  highlightCalendar(dutyDates) {
    for (const dutyDate of dutyDates) {
      const dateObj = document.getElementById(dutyDate);
      dateObj.style.backgroundColor = this.color;
      dateObj.classList.toggle('highlighted');

      if (this.colorIsDark) {
        dateObj.style.color = '#f6f7f9';
        dateObj.style.borderColor = '#edeeef';
      }
    }
  }

  clearCalendar(dutyDates) {
    for (const dutyDate of dutyDates) {
      const dateObj = document.getElementById(dutyDate);
      dateObj.style.backgroundColor = 'transparent';
      dateObj.classList.toggle('highlighted');
      dateObj.style.color = '#212529';
      dateObj.style.borderColor = 'transparent';
    }
  }

  get colorIsDark () {
    const darkness_margin = 186;
    const color_darkness = this.calcColorDarkness();
    return color_darkness < darkness_margin
  }

  calcColorDarkness() {
    const red = parseInt('0x'.concat(this.color.slice(1, 3)));
    const green = parseInt('0x'.concat(this.color.slice(3, 5)));
    const blue = parseInt('0x'.concat(this.color.slice(5, 7)));

    // Formula is from here: https://stackoverflow.com/a/3943023/5726446
    return red * 0.299 + green * 0.587 + blue * 0.114;
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
