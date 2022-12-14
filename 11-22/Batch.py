def generate_batches(batch_size, features, labels):
    output_batches = []
    sample_size = len(features)
    
    for start_i in range(0, sample_size, batch_size):
        end_i = start_i + batch_size
        batch = [features[start_i:end_i], labels[start_i:end_i]]
        output_batches.append(batch)
    return output_batches