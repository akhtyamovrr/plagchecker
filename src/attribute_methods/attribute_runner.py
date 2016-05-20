def compare(metrics, new_source, sources_metric_values, max_allowed):
    """
    Runs metric modules on new source and compares with existing ones
    :param metrics: list of metric modules. They should implement count(source_string) and return integer value
    :param new_source: source to be checked by metrics
    :param sources_metric_values: existing sources metrics
    :param max_allowed: max allowed similarity of result metrics to be not plagiarism for attributes check
    :return: list of sources that may be plagiarism and should be checked by more reliable algorithm
    """
    metrics_count = 0
    for metric in metrics:
        metrics_count += metric.count(new_source)
    metrics_count /= len(metrics)
    further_comparison = {}
    for key in sources_metric_values.keys():
        ratio = abs(metrics_count / sources_metric_values[key])
        if ratio > 1:
            ratio = 1 / ratio
        if ratio > max_allowed:
            further_comparison[key] = sources_metric_values[key]
    return further_comparison
