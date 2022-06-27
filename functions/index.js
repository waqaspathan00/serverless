const functions = require("firebase-functions");
const cors = require('cors')({origin: "localhost:3000"});

exports.helloWorld = functions.https.onRequest((request, response) => {

    cors(req, res, () => {
        res.status(200).json([
            {food: "pizza"}
        ]).end()
    })

});
