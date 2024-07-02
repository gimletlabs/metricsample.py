# Gimlet Metrics GRPC Sample Code

This project provides a Python client for interacting with the Gimlet's control plane to fetch metrics. The client sends a `RangeQuery` request to the server and displays the resulting metric data in a formatted table.

## Features

- Connects to a gRPC server with SSL/TLS.
- Sends a `RangeQuery` request with custom query and time window parameters.
- Displays metric data in a tabulated format.

## Prerequisites

- Python 3.6+
- `grpcio` and `grpcio-tools` packages
- `tabulate` package
- `colored` package

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/metricsreader_client.git
   cd metricsreader_client
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt   
   ```
   
## Usage
1. Set the GML_API_KEY environment variable with your API key:

``` bash
export GML_API_KEY=your_api_key_here
```

2. Run the client:

``` bash
python client.py [--server_addr <server_address>] [--query <query>] [--relative <relative_time_window>]
```
- --server_addr: (Optional) The address of the gRPC server (e.g., app.gimletlabs.ai:443).
- --query: (Optional) The PromQL query string (default: gml_gem_image_quality_brisque_score).
- --relative: (Optional) The relative time window to query (default: -5m).

### Example

``` bash
export GML_API_KEY=your_api_key_here
python client.py app.gimletlabs.ai:443 --query "gml_gem_image_quality_brisque_score" --relative "-10m"
```

## Code Overview
- client.py: The main script that sends the gRPC request and displays the results.
- metricsreader/: Directory containing generated protobuf files.

## License
This project is licensed under the Apache License. See the [LICENSE](LICENSE) file for details.





