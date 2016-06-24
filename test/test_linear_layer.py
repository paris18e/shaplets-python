from __future__ import division
from __future__ import print_function
import numpy as np
from layers.linear_layer import LinearLayer
from util import utils


def test_fc_layer_initialization():
    n_inputs = 15
    n_outputs = 4
    fc_layer = LinearLayer(n_inputs, n_outputs)
    W, W_0 = fc_layer.get_params()
    assert (W.shape == (n_outputs, n_inputs))
    assert (W_0.shape == (n_outputs, 1))


def test_forward():
    n_inputs = 15
    n_outputs = 4
    # create a layer
    fc_layer = LinearLayer(n_inputs, n_outputs)
    # initialize weights
    W = np.ones((n_outputs, n_inputs))
    W_0 = np.ones((n_outputs, 1))
    fc_layer.set_weights(W, W_0)
    # create a layer input
    layer_input = np.ones((1, n_inputs))
    # execute the layer
    layer_output = fc_layer.forward(layer_input)
    # compare the layer output to the expected one
    expected_output = np.array([[16., 16., 16., 16.]])
    assert (np.array_equal(layer_output, expected_output))


def test_backword():
    """
    :return:
    """
    # create a layer
    n_inputs = 15
    n_outputs = 4
    # create a layer
    fc_layer = LinearLayer(n_inputs, n_outputs)
    # create a layer input
    layer_input = np.random.normal(loc=0, scale=1, size=(1, n_inputs))
    # create dL_layer_doutput
    dL_layer_output = np.random.normal(loc=0, scale=1, size=(1, n_outputs))
    # do a forward and a backward pass
    fc_layer.forward(layer_input)
    dL_input = fc_layer.backward(dL_layer_output)
    # verify dL_dinput ######
    doutput_input_truth = utils.approximate_derivative(fc_layer.forward, layer_input, n_outputs,
                                                       h=0.01)  # n_outputs X n_inputs
    dL_input_truth = np.dot(dL_layer_output, doutput_input_truth)
    result = np.isclose(dL_input, dL_input_truth)
    assert result.all()
