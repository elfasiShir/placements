    function filter(element) {
        var value = $(element).val().toLowerCase();

        $("#theList > li").each(function() {
            if ($(this).text().toLowerCase().search(value) > -1) {
                $(this).show();
            }
            else {
                $(this).hide();
            }
        });
    }