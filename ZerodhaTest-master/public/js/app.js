angular
  .module("BSEApp", ["ngMaterial", "md.data.table"])

  .config([
    "$mdThemingProvider",
    function($mdThemingProvider) {
      $mdThemingProvider.definePalette('amazingPaletteName', {
        '50': 'ffebee',
        '100': 'ffcdd2',
        '200': 'ef9a9a',
        '300': 'e57373',
        '400': 'ef5350',
        '500': 'f44336',
        '600': 'e53935',
        '700': 'd32f2f',
        '800': 'c62828',
        '900': 'b71c1c',
        'A100': 'ff8a80',
        'A200': 'ff5252',
        'A400': 'ff1744',
        'A700': 'd50000',
        'contrastDefaultColor': 'light',
        'contrastDarkColors': ['50', '100', 
         '200', '300', '400', 'A100'],
        'contrastLightColors': undefined    
      });
      $mdThemingProvider.theme('default')
      .primaryPalette('amazingPaletteName')

    }
  ])

  .controller("nutritionController", [
    "$mdEditDialog",
    "$q",
    "$scope",
    "$timeout",
    "$http",
    "$sce",

    function($mdEditDialog, $q, $scope, $timeout, $http, $sce) {
      "use strict";
      var bookmark;
      $scope.selected = [];
      $scope.limitOptions = [5, 10, 15];
      $scope.getStocks = getStocks;
      $scope.searchStocks = searchStocks;
      $scope.updateStocks = updateStocks;
      $scope.operationDetails = getOperationDetails;

      $scope.query = {
        order: "name",
        limit: 10,
        page: 1,
        filter: ""
      };
      $scope.highlight = function(text, search) {
        if (!search) {
          return $sce.trustAsHtml(text);
        }
        return $sce.trustAsHtml(
          text.replace(
            new RegExp(search, "gi"),
            '<span class="highlightedText">$&</span>'
          )
        );
      };

      $scope.filter = {
        options: {
          debounce: 500
        }
      };

      $scope.toggleLimitOptions = function() {
        $scope.limitOptions = $scope.limitOptions ? undefined : [5, 10, 15];
      };

      activate();
      getOperationDetails();

      function activate() {
        var promises = [getStocks()];
        return $q.all(promises);
      }

      function searchStocks(query) {
        if (query) {
          $scope.promise = $http
            .get("/stocks/search", {
              params: { name: query }
            })
            .then(function(data) {
              $scope.stocks = data;
            });
        }
      }

      function updateStocks(){
        $scope.promise = $http.get("/update").then(function(data) {
          $scope.stocks = data;
          activate();
          getOperationDetails();
        });
        
      }

      function getStocks() {
        $scope.promise = $http.get("/stocks").then(function(data) {
          $scope.stocks = data;
        });
      }
      
      function getOperationDetails() {
        $scope.promise = $http.get("/operation").then(function(data) {
          $scope._date = data.data[0];
          $scope._time = data.data[1];
        });
      }


      $scope.removeFilter = function() {
        $scope.filter.show = false;
        $scope.query.filter = "";

        if ($scope.filter.form.$dirty) {
          $scope.filter.form.$setPristine();
        }
        getStocks();
      };

      $scope.$watch("query.filter", function(newValue, oldValue) {
        if (!oldValue) {
          bookmark = $scope.query.page;
        }

        if (newValue !== oldValue) {
          $scope.query.page = 1;
        }

        if (!newValue) {
          $scope.query.page = bookmark;
        }
        if (newValue || oldValue) {
          $scope.searchStocks($scope.query.filter);
        }
      });
    }
  ]);
