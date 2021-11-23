from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import BernoulliNB, GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.semi_supervised import LabelSpreading
from sklearn.svm import SVC
from sklearn_genetic import GASearchCV
from sklearn_genetic.space import Continuous, Categorical, Integer
from sklearn.model_selection import StratifiedKFold


def apply_all(X_train, y_train, X_test, y_test, verbose):
    lst = [
        get_svc_genetic_classifier(X_train, y_train, verbose),
        get_gaussian_nb_genetic_classifier(X_train, y_train, verbose),
        get_bernoulli_nb_genetic_classifier(X_train, y_train, verbose),
        get_label_spreading_genetic_classifier(X_train, y_train, verbose),
        get_random_forest_genetic_classifier(X_train, y_train, verbose),
        get_knn_genetic_classifier(X_train, y_train, verbose),
        # get_lgb_genetic_classifier(X_train, y_train, verbose),
    ]
    lst.sort(key=lambda x: x.best_score_, reverse=True)
    if verbose:
        for item in lst:
            print_estimator_essential_info(item, X_test, y_test)
    return lst[0]


def get_svc_genetic_classifier(X_train, y_train, verbose):
    clf = SVC()
    estimator = generate_estimator(
        clf,
        svc_params(),
        verbose,
    )
    estimator.fit(X_train, y_train)
    return estimator


def get_label_spreading_genetic_classifier(X_train, y_train, verbose):
    clf = LabelSpreading()
    estimator = generate_estimator(
        clf,
        label_spreading_params(),
        verbose,
    )
    estimator.fit(X_train, y_train)
    return estimator


def get_lgb_genetic_classifier(X_train, y_train, verbose):
    clf = LGBMClassifier()
    estimator = generate_estimator(
        clf,
        lgb_params(),
        verbose,
    )
    estimator.fit(X_train, y_train)
    return estimator


def get_gaussian_nb_genetic_classifier(X_train, y_train, verbose):
    clf = GaussianNB()
    estimator = generate_estimator(
        clf,
        gaussian_nb_params(),
        verbose,
    )
    estimator.fit(X_train, y_train)
    return estimator


def get_bernoulli_nb_genetic_classifier(X_train, y_train, verbose):
    clf = BernoulliNB()
    estimator = generate_estimator(
        clf,
        bernoulli_nb_params(),
        verbose,
    )
    estimator.fit(X_train, y_train)
    return estimator


def get_random_forest_genetic_classifier(X_train, y_train, verbose):
    clf = RandomForestClassifier()
    estimator = generate_estimator(clf, random_forest_params(), verbose)
    estimator.fit(X_train, y_train)
    return estimator


def get_knn_genetic_classifier(X_train, y_train, verbose):
    clf = KNeighborsClassifier()
    estimator = generate_estimator(clf, knn_params(), verbose)
    estimator.fit(X_train, y_train)
    return estimator


def generate_estimator(clf,
                       param_grid,
                       verbose,
                       population_size=10,
                       generations=35
                       ):
    cv = StratifiedKFold(n_splits=3, shuffle=True)
    evolved_estimator = GASearchCV(estimator=clf,
                                   cv=cv,
                                   param_grid=param_grid,
                                   scoring='accuracy',
                                   population_size=population_size,
                                   generations=generations,
                                   tournament_size=3,
                                   elitism=True,
                                   crossover_probability=0.8,
                                   mutation_probability=0.1,
                                   criteria='max',
                                   algorithm='eaMuPlusLambda',
                                   n_jobs=-1,
                                   verbose=verbose,
                                   keep_top_k=4)
    return evolved_estimator


def print_estimator_essential_info(estimator, X_test, y_test):
    y_predict_ga = estimator.predict(X_test)
    accuracy = accuracy_score(y_test, y_predict_ga)
    print(
        f'--- Generic Algorithm Results ---\n'
        f'Best Score {estimator.best_score_} -'
        f' Parameters {estimator.best_params_}\n'
        f'Accuracy: {accuracy}'
    )


def bernoulli_nb_params():
    return {
        'fit_prior': Categorical([True, False]),
        'binarize': Continuous(0.0, 1.0),
        'alpha': Continuous(0.0, 1.0)
    }


def gaussian_nb_params():
    return {
        'var_smoothing': Continuous(0.0000000001, 0.00000001),
    }


def knn_params():
    return {
        'weights': Categorical(['uniform', 'distance']),
        'metric': Categorical(['minkowski', 'euclidean', 'manhattan', 'chebyshev']),
        'n_neighbors': Integer(1, 10),
        'leaf_size': Integer(1, 60),
        'p': Integer(1, 4)
    }


def random_forest_params():
    return {'min_weight_fraction_leaf': Continuous(0.01, 0.5, distribution='log-uniform'),
            'bootstrap': Categorical([True, False]),
            'max_depth': Integer(10, 30),
            'max_leaf_nodes': Integer(2, 35),
            'n_estimators': Integer(100, 300)}


def label_spreading_params():
    return {
        'kernel': Categorical(['knn', 'rbf']),
        'n_neighbors': Integer(3, 21),
        'max_iter': Integer(20, 60),
    }


def svc_params():
    return {
        'kernel': Categorical(['linear', 'poly', 'rbf', 'sigmoid']),
        'gamma': Categorical(['scale', 'auto']),
        'coef0': Continuous(0.0, 1.0),
        'shrinking': Categorical([True, False]),
        'probability': Categorical([True, False]),
        'max_iter': Integer(1000, 10000),
    }


def lgb_params():
    return {'learning_rate ': Continuous(0.1, 0.5, distribution='log-uniform'),
            'boosting_type': Categorical(['gbdt', 'dart', 'dart', 'goss', 'rf']),
            'num_leaves ': Integer(1, 62),
            'n_estimators': Integer(50, 300),
            'subsample_for_bin ': Integer(100000, 300000),
            }
