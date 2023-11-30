document.addEventListener("DOMContentLoaded", () => {
    const form = document.forms[0];
    const startDateInput = document.getElementById("start-date");
    const endDateInput = document.getElementById("end-date");
    const error = document.getElementById("error");
    const today = new Date().toLocaleDateString('en-ca').padStart(9, "0");

    form.addEventListener("submit", (event) => {
        event.preventDefault(); // stop the form from submitting

        if (startDateInput.value == "" && endDateInput.value == "") {
            form.submit();
            return;
        }
        error.innerHTML = "";
        if (startDateInput.value != "")
        {
            if (new Date(startDateInput.value).toLocaleDateString('en-ca').padStart(9,"0") > today ) {
            error.innerHTML = "Start date cannot be after today  date " + today;
            return;
        }
        }
        error.innerHTML = "";
        if (endDateInput.value != "")
        {
        if (startDateInput.value > endDateInput.value) {
            error.innerHTML = "End date cannot be before start date!";
            return;
        }
    }
    error.innerHTML = "";
        form.submit();
    });
});