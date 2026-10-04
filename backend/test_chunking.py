from app.services.chunk_service import chunk_text


sample_text = """
Internet of Things (IoT) is a system of interconnected physical devices
that communicate and exchange data over networks. These devices may
include sensors, appliances, vehicles, and other physical objects.

IoT systems commonly use sensors to collect information from the
environment. The collected data can then be transmitted to servers or
cloud platforms for processing and analysis.

Applications of IoT include smart homes, healthcare, agriculture,
industrial automation, transportation, and smart cities.
"""


chunks = chunk_text(
    sample_text,
    chunk_size=200,
    chunk_overlap=50
)


for index, chunk in enumerate(chunks, start=1):
    print("=" * 60)
    print(f"CHUNK {index}")
    print("=" * 60)
    print(chunk)