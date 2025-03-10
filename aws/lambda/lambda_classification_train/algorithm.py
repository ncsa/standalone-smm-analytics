import plot
from lambda_classification_train import Classification


def algorithm(array, params):
    """
    wrapper function to put each individual algorithm inside
    :param array: array that contains all the input dataset
    :param params: algorithm specific parameters
    :return: a dictionary of { outputname: output content in memory }
    """

    output = {}

    CF = Classification(array)

    output['uid'] = params['uid']

    fold_scores, text_clf = CF.classify(params['model'])
    output['accuracy'] = fold_scores
    output['pipeline'] = text_clf

    labels = text_clf.classes_
    output['metrics'] = CF.calc_metrics(labels)

    # plot
    output['div_accuracy'] = plot.plot_bar_chart(fold_scores[0], fold_scores[1],
                                        title='10 fold cross validation accuracy score')

    return output