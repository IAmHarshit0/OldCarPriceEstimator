function onPageLoad() {
  console.log("Document Loaded");
  var url = "/get_brand_names";
  // var url = "/api/get_brand_names"
  $.get(url, function (data, status) {
    console.log("Got Response For get_brand_names Request");
    if (data) {
      var brand = data.brand;
      var uibrand = document.getElementById("uibrand");
      $("#uibrand").empty();
      for (var i in brand) {
        var opt = new Option(brand[i]);
        $("#uibrand").append(opt);
      }
    }
  });
}

function get_fuel() {
  var uifuel = document.getElementsByName("fuel");
  for (var i in uifuel) {
    if (uifuel[i].checked) {
      return uifuel[i].value;
    }
  }
  return -1;
}

function get_transmission() {
  var uitransmission = document.getElementsByName("transmission");
  for (var i in uitransmission) {
    if (uitransmission[i].checked) {
      return uitransmission[i].value;
    }
  }
  return -1;
}

function get_owner() {
  var uiowner = document.getElementsByName("owner");
  for (var i in uiowner) {
    if (uiowner[i].checked) {
      return uiowner[i].value;
    }
  }
  return -1;
}

function get_seller() {
  var uiseller = document.getElementsByName("seller");
  for (var i in uiseller) {
    if (uiseller[i].checked) {
      return uiseller[i].value;
    }
  }
  return -1;
}

function onClickEstimatePrice() {
  console.log("Estimated Price Button Clicked");
  var brand = document.getElementById("uibrand");
  var fuel = get_fuel();
  var transmission = get_transmission();
  var owner = get_owner();
  var seller = get_seller();
  var year = document.getElementById("uiyear");
  var km = document.getElementById("uikm");
  var mileage = document.getElementById("uimileage");
  var engine_cc = document.getElementById("uiengine");
  var max_bhp = document.getElementById("uimax");
  var seats = document.getElementById("uiseat");
  var estprice = document.getElementById("uiestimateprice");

  var url = "/predict_car_price";
  // var url = "/api/predict_car_price"
  $.post(
    url,
    {
      year: parseFloat(year.value),
      km: parseFloat(km.value),
      mileage: parseFloat(mileage.value),
      engine_cc: parseFloat(engine_cc.value),
      max_bhp: parseFloat(max_bhp.value),
      seats: parseFloat(seats.value),
      brand: brand.value,
      fuel: fuel,
      transmission: transmission,
      owner: owner,
      seller: seller,
    },
    function (data, status) {
      console.log(data.estimate_price);
      estprice.innerHTML =
        "<div> Rs." + data.estimate_price.toString() + "</div>";
      console.log(status);
    }
  );
}

window.onload = onPageLoad;
