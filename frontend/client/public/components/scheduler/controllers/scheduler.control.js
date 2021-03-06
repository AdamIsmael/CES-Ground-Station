scheduler
  .controller('SchedulerController', function($scope, TLE, AZEL, Mission, $timeout,$interval, $http) {

    $scope.tle = null;
    $scope.tles = null;

    $scope.nextpass = null;
    $scope.nextpasses = [];
    $scope.nextpassesDisplay = [];

    $scope.missionsDisplay = [];


    
    /**
     * Getting true or false if scheduling: to show table load message
     * @type {Object}
     */
     $scope.isSchedulingFn = function() {
        console.log("updating")
        var config = {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }
        }

        $http.get('http://127.0.0.1:8000/api/scheduler/isscheduling', config)
          .then(function successCallback(response, data) {
            if(response.data == "True") {
              $scope.isScheduling = true
            } else {
              var changed = false
              if($scope.isScheduling == true){
                changed = true
              }
              $scope.isScheduling = false
              if(changed){
                $scope.refreshTables();
              }
            }
          }, function errorCallback(response) {
            console.log(response.status)
        });
     }

     $scope.refreshTables = function(){
        var config = {
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }
        }

        $http.get('http://127.0.0.1:8000/api/nextpass/get', config)
          .then(function successCallback(response, data) {
              $scope.nextpasses = response.data;
          }, function errorCallback(response) {
            console.log(response.status)
        });

        $http.get('http://127.0.0.1:8000/api/mission/get', config)
          .then(function successCallback(response, data) {
              $scope.missions = response.data;
          }, function errorCallback(response) {
            console.log(response.status)
        });
     }

     $interval($scope.isSchedulingFn, 3000, 0, true);

     //$interval($scope.updateTables, 3000, 0, true);

    /**
     * Load in TLE data from Django side
     * @return {[type]} [description]
     */
    $scope.loadSat = function() {
      // Grab TLE from Django 
      TLE.query().$promise.then(function(data) {
        $scope.tles = data;
      });
    };

    /**
     * Load in azimuth and elevation values from Django Models
     */
    $scope.loadAxel = function() {
      // Grabbing AZEL data from Django; under construction
      AZEL.query().$promise.then(function(data) {
        $scope.azel = data;
      });
    };

    /**
     * Download csv from current next pass tables
     */
    $scope.downloadCSV = function() {

      $http({
        method: 'GET',
        url: 'http://localhost:8000/api/csv/missions',
        headers: {
          'Content-Type': 'text/csv'
        },
      }).then(function successCallback(response) {
        // this callback will be called asynchronously
        // when the response is available
        window.location.href = ('http://localhost:8000/api/csv/missions')
        console.log(response)
      }, function errorCallback(response) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
      });
    };



    /**
     * TODO: next passes model in here: the service for this does not have the right URL as the URL is not made yet
     * @return void
     */
    $scope.loadNextPasses = function() {

      var config = {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      }

      $http.get('http://127.0.0.1:8000/api/nextpass/get', config)
        .then(function successCallback(response, data) {
          // this callback will be called asynchronously
          // when the response is available
          console.log("Refreshed nextpasses")

          $scope.nextpasses = response.data;
          $scope.nextpassesDisplay = [].concat($scope.nextpasses);

        }, function errorCallback(response) {
          // called asynchronously if an error occurs
          // or server returns response with an error status.
          console.log("Failed to get scheduled passes")
        });
    }


    $scope.loadNextPasses()

    /**
     * priorities: should default at 2 in dropdown 
     * @type {Array}
     */
    $scope.priorities = [{
      name: "low",
      priority: 1,
    }, {
      name: "default",
      priority: 2,
    }, {
      name: "high",
      priority: 3,
    }];

    /**
     * SatMission object: sat name and priority
     * SatMissions List: containing sat missions objects
     */

    // update table from drop down; will need to take in data from scheduler i.e. table dropdown --> fetch schedule data based on this then 
    // update table from scheduled data


    /**
     * Take in current clicked dropdown inputs: sat name and priority.
     * Pass these to back end to add to current missions. 
     * @return void 
     */
    $scope.updateTable = function() {
      $scope.isScheduling = true;

      // Each mission requires a sat name and a priority
      try {
        $scope.mission = {
          name: $scope.tle.name,
          priority: $scope.priority.priority
        };
      } catch (err) {
        console.log('nothing selected');
      }


      try {
        console.log($scope.mission)
        $http.post('http://127.0.0.1:8000/api/save/mission/', $scope.mission)
          .then(function successCallBack(response) {
              // Succeess is anything between 200 and 299
              $scope.missions = Mission.get().$promise.then(function(data) {
                $scope.missions = data;
              });

              $scope.missionsDisplay = [].concat($scope.missions);
              $scope.loadNextPasses();
            },
            function errorCallBack(response) {
              console.log(response.status + " : " + response.statusText);
            }
          );
      } catch (err) {
        alert("you must first select a satellite and a priority")
      }
      $scope.isScheduling = true;
    };


    //MISSSION TABLE

    $scope.missions = Mission.get().$promise.then(function(data) {
      $scope.missions = data;
    });


    $scope.deleteMission = function(mission) {
      $scope.missionid = mission.id;
      $scope.isScheduling = true;

      var config = {
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
      }

      $http.delete('http://127.0.0.1:8000/api/delete/mission/' + $scope.missionid, config)
          .then(function successCallBack(response) {
              
              $scope.missions = Mission.get().$promise.then(function(data) {
                $scope.missions = data;
              });

              $scope.missionsDisplay = [].concat($scope.missions);

              $scope.loadNextPasses()
            },
            function errorCallBack(response) {
              console.log(response.status + " : " + response.statusText);
            }
          );
        $scope.isScheduling = true;
    };


    /*$scope.deleteMission = function(mission) {
      id = mission.id;
      Mission.delete({
        id: id
      }, (function(resp) {
        console.log(resp);
        removeA($scope.missions, mission)
        $scope.loadNextPasses()
      }))

    function removeA(arr) {
      //What is this?!
      var what, a = arguments,
        L = a.length,
        ax;
      while (L > 1 && arr.length) {
        what = a[--L];
        while ((ax = arr.indexOf(what)) !== -1) {
          arr.splice(ax, 1);
        }
      }
      return arr;
    }*/


    //$interval($scope.reload, 5000);

    // End of controller please leave it alone.
  });