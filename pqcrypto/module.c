#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *crypto_sign_keypair_python(PyObject *self, PyObject *args)
{
    uint8_t *seed;
    uint8_t *pubkey;
    uint8_t *privkey;
    uint8_t *private_key;
    uint8_t *public_key;

    if (!PyArg_ParseTuple(args, "S", &seed))
        return NULL;
    Py_INCREF(seed);
    pubkey = PyMem_Malloc(897);
    privkey = PyMem_Malloc(1281);

    crypto_sign_keypair(privkey, pubkey, seed);

    Py_DECREF(privkey);
    private_key = Py_BuildValue("y#", privkey, 1281);
    Py_DECREF(pubkey);
    public_key = Py_BuildValue("y#", pubkey, 897);

    PyMem_Free(privkey);
    PyMem_Free(pubkey);
    return private_key, public_key;
}

static PyMethodDef pqcryptoMethods[] = {
    { "crypto_sign_keypair", crypto_sign_keypair_python, METH_VARARGS, "crypto_sign_keypair_python" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef pqcryptoModule = {
    PyModuleDef_HEAD_INIT,
    "crypto_sign_keypair",
    "...",
    -1,
    pqcryptoMethods
};

PyMODINIT_FUNC PyInit_pqcrypto(void) {
    return PyModule_Create(&pqcryptoModule);
}
