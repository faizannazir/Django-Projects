$(document).ready(function() {
    // Form submit event
    $('form').submit(function(event) {
      // Prevent form submission
      event.preventDefault();
  
      // Validate form fields
      if (validateForm()) {
        // If form is valid, submit the form
        this.submit();
      }
    });
  
    // Function to validate form fields
    function validateForm() {
      var isValid = true;
  
      // Clear previous error messages
      $('.text-danger').text('');
  
      // Validate first name
      var firstName = $('#first_name').val();
      if (firstName.trim() === '') {
        $('#first_name').next('.text-danger').text('First name is required');
        isValid = false;
      }
  
      // Validate last name
      var lastName = $('#last_name').val();
      if (lastName.trim() === '') {
        $('#last_name').next('.text-danger').text('Last name is required');
        isValid = false;
      }
  
      // Validate email
      var email = $('#email').val();
      if (email.trim() === '') {
        $('#email').next('.text-danger').text('Email is required');
        isValid = false;
      }
  
      // Validate department
      var department = $('#dep').val();
      if (department.trim() === '') {
        $('#dep').next('.text-danger').text('Department is required');
        isValid = false;
      }
  
      // Validate date of birth
      var dateOfBirth = $('#birth').val();
      if (dateOfBirth.trim() === '') {
        $('#birth').next('.text-danger').text('Date of birth is required');
        isValid = false;
      }
  
      // Validate joining date
      var joiningDate = $('#join').val();
      if (joiningDate.trim() === '') {
        $('#join').next('.text-danger').text('Joining date is required');
        isValid = false;
      }
    // Validate picture (if provided)
    var picture = $('#formFile').prop('files')[0];
    if (picture) {
      var allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
      if (allowedTypes.indexOf(picture.type) === -1) {
        $('#formFile').next('.text-danger').text('Invalid image file type');
        isValid = false;
      }
    }
  
      return isValid;
    }
  });
  