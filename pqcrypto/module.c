#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *yespower_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
    PyBytesObject *input;

    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

    yespower_hash((char *)PyBytes_AsString((PyObject*) input), output);

    Py_DECREF(input);
    value = Py_BuildValue("y#", output, 32);

    PyMem_Free(output);
    return value;
}

static PyMethodDef YespowerMethods[] = {
    { "getPoWHash", yespower_getpowhash, METH_VARARGS, "Returns the proof of work hash using yespower" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef YespowerModule = {
    PyModuleDef_HEAD_INIT,
    "yespower_hash",
    "...",
    -1,
    YespowerMethods
};

PyMODINIT_FUNC PyInit_tdc_yespower(void) {
    return PyModule_Create(&YespowerModule);
}
