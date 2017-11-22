function load_products(offset = 0, products_per_page = 10) {
    $.ajax({
        url: 'http://api/products/',
        type: 'POST',
        data: {
            'offset': offset,
            'products_per_page': products_per_page
        },
        dataType: 'json',
        success: function(data) {
            alert(data)
            /*
            data = [
                {
                    name: "Produto A",
                    price: "23,40",
                    brand: "Adidas",
                    created_at: "21-11-2017T00:00:00"
                    updated_At: "21-11-2017T00:00:00"
                }
            ]*/
        },
        error: function(request, error) {
            alert("Request: " + JSON.stringify(request));
        }
    });
}
