#!/usr/bin/env python3

import grpc
import os
import sys
from metricsreader.v1 import metrics_pb2
from metricsreader.v1 import metrics_pb2_grpc
from tabulate import tabulate
import argparse
from colored import attr, fg

def get_range_query_results(server_address, query="gml_gem_image_quality_brisque_score", relative="-5m"):
    # Create SSL credentials using default trusted certificates
    credentials = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel(server_address, credentials)

    stub = metrics_pb2_grpc.MetricsReaderServiceStub(channel)

    api_key = os.getenv("GML_API_KEY")
    metadata = [("x-api-key", api_key)]

    if not api_key or len(api_key)==0:
        print("env GML_API_KEY must be set")
        sys.exit(1)

    request = metrics_pb2.RangeQueryRequest(query=query, relative=relative)
    response = stub.RangeQuery(request, metadata=metadata)

    return response.results

def bold_key(key):
    return f"{attr('bold')}{key}{attr('reset')}"

def display_metric_data(results):
    for metric_data in results:
        print(f"{bold_key('Metric Name')}: {metric_data.name}")
        print(f"{bold_key('Labels')}: {', '.join([f'{bold_key(k)}={v}' for k, v in metric_data.labels.items()])}")
        print()

    rows = []
    for metric_data in results:
        if metric_data.HasField('metric_sample'):
            for time, value in zip(metric_data.metric_sample.times, metric_data.metric_sample.values):
                rows.append([time, value])
        elif metric_data.HasField('histogram_sample'):
            for bucket_end, count in zip(metric_data.histogram_sample.bucket_ends, metric_data.histogram_sample.counts):
                rows.append([bucket_end, count])

    table = tabulate(rows, headers=[bold_key('Time/Bucket End'), bold_key('Value')], tablefmt='grid')
    print(table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="gRPC client to read metrics data from Gimlet")
    parser.add_argument('--server_address', type=str, help="Address of the gRPC server", default="app.gimletlabs.ai:443")
    parser.add_argument('--query', type=str, default="gml_gem_image_quality_brisque_score", help="The PromQL query string")
    parser.add_argument('--relative', type=str, default="-5m", help="The relative time window to query")

    args = parser.parse_args()

    results = get_range_query_results(args.server_address, args.query, args.relative)
    display_metric_data(results)
