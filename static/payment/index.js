$(document).ready(function(){
    $("#rzp-button1").click(function(event){
        event.preventDefault();
        var custName = document.getElementById("custName").value;
        var custContact = document.getElementById("custContact").value;
        var custAdd = document.getElementById("custAdd").value;
        var custCountry = document.getElementById("country").value;
        var custState = document.getElementById("state").value;
        var custPostal = document.getElementById("postCode").value;

        var errorMessages = {
            "custName": "Please enter your name",
            "custContact": "Please enter your contact no.",
            "custAdd": "Please enter your address",
            "country": "Please select your country",
            "state": "Please select your state",
            "postCode": "Please enter your postal code"
        };

        if (custName == "" || custContact == "" || custAdd == "" || custCountry == "" || custState == "" || custPostal == "") {
            var errorMessage = "";
            if (custName == "") {
                errorMessage += errorMessages["custName"] + "\n";
            }
            if (custContact == "") {
                errorMessage += errorMessages["custContact"] + "\n";
            }
            if (custAdd == "") {
                errorMessage += errorMessages["custAdd"] + "\n";
            }
            if (custCountry == "") {
                errorMessage += errorMessages["country"] + "\n";
            }
            if (custState == "") {
                errorMessage += errorMessages["state"] + "\n";
            }
            if (custPostal == "") {
                errorMessage += errorMessages["postCode"] + "\n";
            }
            swal("Alert", errorMessage, "error");
            return false;
        }
        
        else
        {
            
            var options = {
                "key": "rzp_test_CZRnA2Q0OndAes", 
                "amount": razoramount, 
                "currency": "INR",
                "name": "BookStore",
                "description": "Test Transaction",
                "order_id": order_id,
                "handler": function (response){
                    var form = document.getElementById("payment-form");
                    window.location.href = 'http://127.0.0.1:8000/payment/orderplaced?order_id=${response.razorpay_order_id}&payment_id=${response.razorpay_payment_id}&cust_id=${form.elements["custid"].value}'
                },
                "prefill": {
                    "name": custName,
                    "email": email,
                    "contact": custContact
                },
                "theme": {
                    "color": "#3399cc"
                }
            };

            var rzp1 = new Razorpay(options);
            rzp1.on('payment.failed', function (response){
                    alert(response.error.metadata.payment_id);
            });
            rzp1.open();
        }
    });
});


