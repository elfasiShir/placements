import {
    toDateTimeString
} from './utils.js';

function setReportingTime() {
    let date = document.getElementById('input-reporting-date').value;
    let time = document.getElementById('input-reporting-time').value;
    document.getElementById('input-reporting_time-hidden').value = toDateTimeString(date, time);
}

document.getElementById('input-reporting-date').addEventListener('change', () => {
    setReportingTime();
})

document.getElementById('input-reporting-time').addEventListener('change', () => {
    setReportingTime();
})