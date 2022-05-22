export default function handler(request, response) {
    if (request.method === "GET"){
        response.json([
            {food: "pizza"}
        ])
    }
}