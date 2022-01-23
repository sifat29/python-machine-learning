{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "6ddb7235",
   "metadata": {},
   "source": [
    "## import"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1b5c5e9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import datasets\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.neighbors import KNeighborsClassifier\n",
    "import numpy as np\n",
    "from collections import Counter\n",
    "from matplotlib.colors import ListedColormap"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "96439014",
   "metadata": {},
   "source": [
    "## load dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4cc6820c",
   "metadata": {},
   "outputs": [],
   "source": [
    "iris = datasets.load_iris()\n",
    "x = iris.data\n",
    "y = iris.target\n",
    "\n",
    "X_train, x_test, Y_train, y_test = train_test_split(x,y,test_size=0.2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2014be0d",
   "metadata": {},
   "source": [
    "## distance calculator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "03700ec2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def distance_calc(x1, x2):\n",
    "    return np.sqrt(np.sum((x1 - x2) ** 2))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d586c022",
   "metadata": {},
   "source": [
    "## KNN Algorithm class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3e35f360",
   "metadata": {},
   "outputs": [],
   "source": [
    "class KNN:\n",
    "\n",
    "    def __init__(self, k):\n",
    "        self.K = k\n",
    "    \n",
    "    def fit(self, X, Y):\n",
    "        self.X_train = X\n",
    "        self.Y_train = Y\n",
    "    \n",
    "    def predict(self, X):\n",
    "        P_label = [self._predict(sample) for sample in X]\n",
    "        return np.array(P_label)\n",
    "    \n",
    "    def _predict(self, x):\n",
    "        distances = [distance_calc(x, x_train) for x_train in self.X_train]\n",
    "        k_Idx = np.argsort(distances)[: self.K]\n",
    "        k_n_labels = [self.Y_train[i] for i in k_Idx]\n",
    "        most_common = Counter(k_n_labels).most_common(1)\n",
    "        return most_common[0][0]\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e5ab66b2",
   "metadata": {},
   "source": [
    "## implimentation using K=5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a00d6e85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prediction accuracy:  96.66666666666667  %\n"
     ]
    }
   ],
   "source": [
    "k = 5\n",
    "clf = KNN(k=k)\n",
    "clf.fit(X_train, Y_train)\n",
    "predictions = clf.predict(x_test)\n",
    "acc = accuracy = np.sum(predictions == y_test) / len(y_test)*100\n",
    "print(\"Prediction accuracy: \",acc,\" %\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
