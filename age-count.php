<?php
$ch = curl_init('https://coderbyte.com/api/challenge/json/age-counting');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, 0);
$data = curl_exec($ch);
curl_close($ch);

if ($data === FALSE) {
    die("Error occurred while fetching the data.");
}

// Decode the JSON response
$response = json_decode($data, true);

if (json_last_error() !== JSON_ERROR_NONE) {
    die("Error decoding JSON: " . json_last_error_msg());
}

// Check if the data key exists and is a string
if (!isset($response['data']) || !is_string($response['data'])) {
    die("Invalid data format.");
}

// Split the string into items
$items = explode(',', $response['data']);

// Initialize the count for items with age >= 50
$count = 0;

// Process each item
foreach ($items as $item) {
    // Split the item into key-value pairs
    $pairs = explode('=', $item);
    
    if (count($pairs) == 2) {
        // Trim whitespace and extract the key and value
        $key = trim($pairs[0]);
        $value = trim($pairs[1]);
        
        if ($key === 'age' && is_numeric($value) && intval($value) >= 50) {
            $count++;
        }
    }
}

// Print the final count
echo $count;
?>
