#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_32"
#define CYTHON_HEX_VERSION 0x001D20F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC (PYPY_VERSION_HEX >= 0x07030900)
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if defined(PyUnicode_IS_READY)
  #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                              0 : _PyUnicode_Ready((PyObject *)(op)))
  #else
  #define __Pyx_PyUnicode_READY(op)       (0)
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if defined(PyUnicode_IS_READY) && defined(PyUnicode_GET_SIZE)
  #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
  #endif
  #else
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__versace
#define __PYX_HAVE_API__versace
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "versace.pyx",
};

/*--- Type declarations ---*/

/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* RaiseArgTupleInvalid.proto */
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found);

/* RaiseDoubleKeywords.proto */
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name);

/* ParseKeywords.proto */
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[],\
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args,\
    const char* function_name);

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
}
#define __Pyx_GetModuleGlobalNameUncached(var, name)  {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
}
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyIntBinop.proto */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check);
#else
#define __Pyx_PyInt_AddObjC(op1, op2, intval, inplace, zerodivision_check)\
    (inplace ? PyNumber_InPlaceAdd(op1, op2) : PyNumber_Add(op1, op2))
#endif

/* PySequenceContains.proto */
static CYTHON_INLINE int __Pyx_PySequence_ContainsTF(PyObject* item, PyObject* seq, int eq) {
    int result = PySequence_Contains(seq, item);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* GetItemInt.proto */
#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\
    (is_list ? (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL) :\
               __Pyx_GetItemInt_Generic(o, to_py_func(i))))
#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "tuple index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,
                                                     int is_list, int wraparound, int boundscheck);

/* IncludeStringH.proto */
#include <string.h>

/* BytesEquals.proto */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals);

/* UnicodeEquals.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals);

/* PyObjectFormatSimple.proto */
#if CYTHON_COMPILING_IN_PYPY
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#elif PY_MAJOR_VERSION < 3
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyString_CheckExact(s)) ? PyUnicode_FromEncodedObject(s, NULL, "strict") :\
        PyObject_Format(s, f))
#elif CYTHON_USE_TYPE_SLOTS
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyLong_CheckExact(s)) ? PyLong_Type.tp_str(s) :\
        likely(PyFloat_CheckExact(s)) ? PyFloat_Type.tp_str(s) :\
        PyObject_Format(s, f))
#else
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#endif

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* JoinPyUnicode.proto */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      Py_UCS4 max_char);

/* None.proto */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname);

/* PyObjectSetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
#define __Pyx_PyObject_DelAttrStr(o,n) __Pyx_PyObject_SetAttrStr(o, n, NULL)
static CYTHON_INLINE int __Pyx_PyObject_SetAttrStr(PyObject* obj, PyObject* attr_name, PyObject* value);
#else
#define __Pyx_PyObject_DelAttrStr(o,n)   PyObject_DelAttr(o,n)
#define __Pyx_PyObject_SetAttrStr(o,n,v) PyObject_SetAttr(o,n,v)
#endif

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* ListCompAppend.proto */
#if CYTHON_USE_PYLIST_INTERNALS && CYTHON_ASSUME_SAFE_MACROS
static CYTHON_INLINE int __Pyx_ListComp_Append(PyObject* list, PyObject* x) {
    PyListObject* L = (PyListObject*) list;
    Py_ssize_t len = Py_SIZE(list);
    if (likely(L->allocated > len)) {
        Py_INCREF(x);
        PyList_SET_ITEM(list, len, x);
        __Pyx_SET_SIZE(list, len + 1);
        return 0;
    }
    return PyList_Append(list, x);
}
#else
#define __Pyx_ListComp_Append(L,x) PyList_Append(L,x)
#endif

/* ObjectGetItem.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject *__Pyx_PyObject_GetItem(PyObject *obj, PyObject* key);
#else
#define __Pyx_PyObject_GetItem(obj, key)  PyObject_GetItem(obj, key)
#endif

/* UnpackUnboundCMethod.proto */
typedef struct {
    PyObject *type;
    PyObject **method_name;
    PyCFunction func;
    PyObject *method;
    int flag;
} __Pyx_CachedCFunction;

/* CallUnboundCMethod1.proto */
static PyObject* __Pyx__CallUnboundCMethod1(__Pyx_CachedCFunction* cfunc, PyObject* self, PyObject* arg);
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_CallUnboundCMethod1(__Pyx_CachedCFunction* cfunc, PyObject* self, PyObject* arg);
#else
#define __Pyx_CallUnboundCMethod1(cfunc, self, arg)  __Pyx__CallUnboundCMethod1(cfunc, self, arg)
#endif

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* SliceObject.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(
        PyObject* obj, Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** py_start, PyObject** py_stop, PyObject** py_slice,
        int has_cstart, int has_cstop, int wraparound);

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* RaiseTooManyValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected);

/* RaiseNeedMoreValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index);

/* IterFinish.proto */
static CYTHON_INLINE int __Pyx_IterFinish(void);

/* UnpackItemEndCheck.proto */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected);

/* ListAppend.proto */
#if CYTHON_USE_PYLIST_INTERNALS && CYTHON_ASSUME_SAFE_MACROS
static CYTHON_INLINE int __Pyx_PyList_Append(PyObject* list, PyObject* x) {
    PyListObject* L = (PyListObject*) list;
    Py_ssize_t len = Py_SIZE(list);
    if (likely(L->allocated > len) & likely(len > (L->allocated >> 1))) {
        Py_INCREF(x);
        PyList_SET_ITEM(list, len, x);
        __Pyx_SET_SIZE(list, len + 1);
        return 0;
    }
    return PyList_Append(list, x);
}
#else
#define __Pyx_PyList_Append(L,x) PyList_Append(L,x)
#endif

/* RaiseException.proto */
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause);

/* PyIntBinop.proto */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_SubtractObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check);
#else
#define __Pyx_PyInt_SubtractObjC(op1, op2, intval, inplace, zerodivision_check)\
    (inplace ? PyNumber_InPlaceSubtract(op1, op2) : PyNumber_Subtract(op1, op2))
#endif

/* PyIntCompare.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_NeObjC(PyObject *op1, PyObject *op2, long intval, long inplace);

/* PyIntCompare.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, long intval, long inplace);

/* DictGetItem.proto */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key);
#define __Pyx_PyObject_Dict_GetItem(obj, name)\
    (likely(PyDict_CheckExact(obj)) ?\
     __Pyx_PyDict_GetItem(obj, name) : PyObject_GetItem(obj, name))
#else
#define __Pyx_PyDict_GetItem(d, key) PyObject_GetItem(d, key)
#define __Pyx_PyObject_Dict_GetItem(obj, name)  PyObject_GetItem(obj, name)
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* ImportFrom.proto */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* SetNameInClass.proto */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* CalculateMetaclass.proto */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases);

/* Py3ClassCreate.proto */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name, PyObject *qualname,
                                           PyObject *mkw, PyObject *modname, PyObject *doc);
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases, PyObject *dict,
                                      PyObject *mkw, int calculate_metaclass, int allow_py2_metaclass);

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'versace' */
#define __Pyx_MODULE_NAME "versace"
extern int __pyx_module_is_main_versace;
int __pyx_module_is_main_versace = 0;

/* Implementation of 'versace' */
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_input;
static PyObject *__pyx_builtin_IndexError;
static PyObject *__pyx_builtin_open;
static PyObject *__pyx_builtin_KeyboardInterrupt;
static PyObject *__pyx_builtin_range;
static PyObject *__pyx_builtin_KeyError;
static const char __pyx_k_[] = "{";
  static const char __pyx_k_C[] = "C";
  static const char __pyx_k_d[] = "-d";
  static const char __pyx_k_e[] = "e";
  static const char __pyx_k_f[] = "f";
  static const char __pyx_k_i[] = "i";
  static const char __pyx_k_m[] = "-m";
  static const char __pyx_k_n[] = "\\n";
  static const char __pyx_k_r[] = "r";
  static const char __pyx_k_t[] = "\\t";
  static const char __pyx_k_v[] = ".v";
  static const char __pyx_k_w[] = "w";
  static const char __pyx_k_y[] = "y";
  static const char __pyx_k_0m[] = "\033[0m";
  static const char __pyx_k_IO[] = "IO";
  static const char __pyx_k__2[] = "";
  static const char __pyx_k__4[] = ":";
  static const char __pyx_k__5[] = "\n";
  static const char __pyx_k_in[] = "in";
  static const char __pyx_k_io[] = "io";
  static const char __pyx_k_nt[] = "nt";
  static const char __pyx_k_os[] = "os";
  static const char __pyx_k_py[] = ".py";
  static const char __pyx_k_rw[] = "rw";
  static const char __pyx_k__12[] = "[";
  static const char __pyx_k__14[] = "]";
static const char __pyx_k__16[] = "}";
static const char __pyx_k__17[] = "{}";
static const char __pyx_k__20[] = " ";
static const char __pyx_k__21[] = ".";
static const char __pyx_k__22[] = "\\";
static const char __pyx_k__25[] = "\"";
static const char __pyx_k__26[] = "'";
static const char __pyx_k__27[] = "<";
static const char __pyx_k__28[] = ",";
static const char __pyx_k__29[] = ")\n";
static const char __pyx_k__33[] = "\r";
static const char __pyx_k__34[] = "\t";
static const char __pyx_k__35[] = "   ";
static const char __pyx_k__42[] = "    ";
static const char __pyx_k__43[] = "//";
static const char __pyx_k__44[] = ";";
static const char __pyx_k__50[] = "    {}";
static const char __pyx_k__51[] = "^";
static const char __pyx_k__52[] = "(";
static const char __pyx_k__53[] = ")";
static const char __pyx_k__71[] = ", ";
static const char __pyx_k_cls[] = "cls";
static const char __pyx_k_def[] = "def";
static const char __pyx_k_dim[] = "dim";
static const char __pyx_k_doc[] = "__doc__";
static const char __pyx_k_end[] = " end=\"";
static const char __pyx_k_get[] = "get";
static const char __pyx_k_inc[] = "inc";
static const char __pyx_k_inp[] = "inp";
static const char __pyx_k_int[] = "int";
static const char __pyx_k_out[] = "out";
static const char __pyx_k_r_2[] = "\\r";
static const char __pyx_k_red[] = "red";
static const char __pyx_k_str[] = "str";
static const char __pyx_k_sys[] = "sys";
static const char __pyx_k_tab[] = "tab";
static const char __pyx_k_tmp[] = ".tmp";
static const char __pyx_k_var[] = "var";
static const char __pyx_k_args[] = "args";
static const char __pyx_k_argv[] = "argv";
static const char __pyx_k_blue[] = "blue";
static const char __pyx_k_bold[] = "bold";
static const char __pyx_k_call[] = "call";
static const char __pyx_k_code[] = "code";
static const char __pyx_k_cyan[] = "cyan";
static const char __pyx_k_dict[] = ": dict";
static const char __pyx_k_elif[] = "elif";
static const char __pyx_k_endl[] = "endl";
static const char __pyx_k_exit[] = "exit";
static const char __pyx_k_file[] = "file";
static const char __pyx_k_from[] = "from";
static const char __pyx_k_func[] = "func";
static const char __pyx_k_incl[] = "incl";
static const char __pyx_k_init[] = "__init__";
static const char __pyx_k_json[] = "json";
static const char __pyx_k_left[] = "left";
static const char __pyx_k_line[] = "line";
static const char __pyx_k_list[] = ": list";
static const char __pyx_k_main[] = "main(";
static const char __pyx_k_name[] = "name";
static const char __pyx_k_newl[] = "newl";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_path[] = "path";
static const char __pyx_k_repr[] = "repr";
static const char __pyx_k_rich[] = "rich";
static const char __pyx_k_self[] = "self";
static const char __pyx_k_sort[] = "sort";
static const char __pyx_k_tabs[] = "tabs";
static const char __pyx_k_temp[] = "temp";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_text[] = "text";
static const char __pyx_k_time[] = "time";
static const char __pyx_k_41_1m[] = "\033[41;1m";
static const char __pyx_k_4_0_0[] = "4.0.0";
static const char __pyx_k_black[] = "black";
static const char __pyx_k_blink[] = "blink";
static const char __pyx_k_brace[] = "brace";
static const char __pyx_k_build[] = "build";
static const char __pyx_k_catch[] = "catch";
static const char __pyx_k_class[] = "class";
static const char __pyx_k_clear[] = "clear";
static const char __pyx_k_close[] = "close";
static const char __pyx_k_end_2[] = "end";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_error[] = "error";
static const char __pyx_k_files[] = "files";
static const char __pyx_k_final[] = "final";
static const char __pyx_k_float[] = "float";
static const char __pyx_k_green[] = "green";
static const char __pyx_k_index[] = "index";
static const char __pyx_k_innit[] = "__innit__";
static const char __pyx_k_input[] = "input";
static const char __pyx_k_lexer[] = "lexer";
static const char __pyx_k_lines[] = "lines";
static const char __pyx_k_lower[] = "lower";
static const char __pyx_k_mkdir[] = "mkdir";
static const char __pyx_k_parse[] = "parse";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_range[] = "range";
static const char __pyx_k_right[] = "right";
static const char __pyx_k_shell[] = "shell";
static const char __pyx_k_sleep[] = "sleep";
static const char __pyx_k_space[] = "space";
static const char __pyx_k_split[] = "split";
static const char __pyx_k_strip[] = "strip";
static const char __pyx_k_style[] = " style=\"";
static const char __pyx_k_tmp_2[] = ".tmp\"";
static const char __pyx_k_white[] = "white";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_C_func[] = "C.func";
static const char __pyx_k_IO_inp[] = "IO.inp";
static const char __pyx_k_Module[] = "  Module ";
static const char __pyx_k_center[] = "center";
static const char __pyx_k_colors[] = "colors";
static const char __pyx_k_except[] = "except";
static const char __pyx_k_exists[] = "exists";
static const char __pyx_k_exit_2[] = "__exit__";
static const char __pyx_k_format[] = "format";
static const char __pyx_k_from_2[] = "_from";
static const char __pyx_k_hidden[] = "hidden";
static const char __pyx_k_import[] = "import";
static const char __pyx_k_italic[] = "italic";
static const char __pyx_k_main_2[] = "main";
static const char __pyx_k_main_3[] = "__main__";
static const char __pyx_k_module[] = "module";
static const char __pyx_k_name_2[] = "__name__";
static const char __pyx_k_output[] = "output";
static const char __pyx_k_public[] = "public";
static const char __pyx_k_remove[] = "remove";
static const char __pyx_k_return[] = "return";
static const char __pyx_k_rmtree[] = "rmtree";
static const char __pyx_k_rstrip[] = "rstrip";
static const char __pyx_k_shutil[] = "shutil";
static const char __pyx_k_styles[] = "styles";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_yellow[] = "yellow";
static const char __pyx_k_C_brace[] = "C.brace";
static const char __pyx_k_C_catch[] = "C.catch";
static const char __pyx_k_C_class[] = "C.class_";
static const char __pyx_k_Version[] = "Version";
static const char __pyx_k_build_2[] = "build\\";
static const char __pyx_k_build_3[] = "build/";
static const char __pyx_k_class_2[] = "class_";
static const char __pyx_k_do_once[] = "do_once";
static const char __pyx_k_else_if[] = "else if";
static const char __pyx_k_include[] = "include";
static const char __pyx_k_input_2[] = " = input()";
static const char __pyx_k_justify[] = "justify";
static const char __pyx_k_listdir[] = "listdir";
static const char __pyx_k_magenta[] = "magenta";
static const char __pyx_k_numtabs[] = "numtabs";
static const char __pyx_k_prepare[] = "__prepare__";
static const char __pyx_k_print_2[] = "print(";
static const char __pyx_k_print_3[] = "print(\"";
static const char __pyx_k_py_code[] = "py_code";
static const char __pyx_k_replace[] = "replace";
static const char __pyx_k_reverse[] = "reverse";
static const char __pyx_k_starter[] = "starter";
static const char __pyx_k_symobol[] = "symobol";
static const char __pyx_k_versace[] = "versace";
static const char __pyx_k_C_public[] = "C.public";
static const char __pyx_k_IO_error[] = "IO.error";
static const char __pyx_k_KeyError[] = "KeyError";
static const char __pyx_k_additive[] = "additive";
static const char __pyx_k_compiler[] = "compiler";
static const char __pyx_k_def_main[] = "def main";
static const char __pyx_k_endswith[] = "endswith";
static const char __pyx_k_endtypes[] = "endtypes";
static const char __pyx_k_filename[] = "filename";
static const char __pyx_k_import_2[] = "__import__";
static const char __pyx_k_inc_incl[] = "inc.incl";
static const char __pyx_k_int_main[] = "int main()";
static const char __pyx_k_module_2[] = "__module__";
static const char __pyx_k_newlines[] = "newlines";
static const char __pyx_k_qualname[] = "__qualname__";
static const char __pyx_k_requests[] = "requests";
static const char __pyx_k_response[] = "response";
static const char __pyx_k_strftime[] = "strftime";
static const char __pyx_k_tag_name[] = "tag_name";
static const char __pyx_k_temp_src[] = "temp\\src";
static const char __pyx_k_C_else_if[] = "C.else_if";
static const char __pyx_k_Exception[] = "Exception: ";
static const char __pyx_k_IO___init[] = "IO.__init__";
static const char __pyx_k_IO_output[] = "IO.output";
static const char __pyx_k_datatypes[] = "datatypes";
static const char __pyx_k_decomplie[] = "decomplie";
static const char __pyx_k_else_if_2[] = "else_if";
static const char __pyx_k_foundMain[] = "foundMain";
static const char __pyx_k_in_module[] = "in_module";
static const char __pyx_k_inc__from[] = "inc._from";
static const char __pyx_k_int_input[] = " = int(input())";
static const char __pyx_k_justify_2[] = " justify=\"";
static const char __pyx_k_localtime[] = "localtime";
static const char __pyx_k_metaclass[] = "__metaclass__";
static const char __pyx_k_music_mp3[] = "music.mp3";
static const char __pyx_k_new_final[] = "new_final";
static const char __pyx_k_org_final[] = "org_final";
static const char __pyx_k_playsound[] = "playsound";
static const char __pyx_k_readlines[] = "readlines";
static const char __pyx_k_statement[] = "statement";
static const char __pyx_k_str_input[] = " = str(input())";
static const char __pyx_k_underline[] = "underline";
static const char __pyx_k_IndexError[] = "IndexError";
static const char __pyx_k_bright_red[] = "bright_red";
static const char __pyx_k_def_main_2[] = "def main()";
static const char __pyx_k_music_path[] = "music_path";
static const char __pyx_k_startswith[] = "startswith";
static const char __pyx_k_statements[] = "statements";
static const char __pyx_k_subprocess[] = "subprocess";
static const char __pyx_k_temp_src_2[] = "temp\\src\\";
static const char __pyx_k_temp_src_3[] = "temp/src/";
static const char __pyx_k_temp_src_4[] = "temp/src";
static const char __pyx_k_FATEL_ERROR[] = "FATEL ERROR:";
static const char __pyx_k_bright_blue[] = "bright_blue";
static const char __pyx_k_bright_cyan[] = "bright_cyan";
static const char __pyx_k_create_temp[] = "create_temp";
static const char __pyx_k_d_m_Y_H_M_S[] = "%d-%m-%Y %H-%M-%S";
static const char __pyx_k_delete_temp[] = "delete_temp";
static const char __pyx_k_float_input[] = " = float(input())";
static const char __pyx_k_module_path[] = "module_path";
static const char __pyx_k_pip_install[] = "pip install ";
static const char __pyx_k_status_code[] = "status_code";
static const char __pyx_k_versace_pyx[] = "versace.pyx";
static const char __pyx_k_41m_30mError[] = "\033[41m\033[30mError: ";
static const char __pyx_k_bright_black[] = "bright_black";
static const char __pyx_k_bright_green[] = "bright_green";
static const char __pyx_k_bright_white[] = "bright_white";
static const char __pyx_k_current_time[] = "current_time";
static const char __pyx_k_from_include[] = "from include *";
static const char __pyx_k_music_option[] = "music_option";
static const char __pyx_k_41_1mBuilding[] = "\033[41;1mBuilding";
static const char __pyx_k_Error_Missing[] = "Error: Missing \"}\"";
static const char __pyx_k_bright_yellow[] = "bright_yellow";
static const char __pyx_k_Format_must_be[] = "  Format must be:";
static const char __pyx_k_INVALID_MODULE[] = "INVALID MODULE";
static const char __pyx_k_INVALID_SYNTAX[] = "INVALID SYNTAX";
static const char __pyx_k_bright_magenta[] = "bright_magenta";
static const char __pyx_k_does_not_exist[] = " does not exist.";
static const char __pyx_k_FileExistsError[] = "FileExistsError";
static const char __pyx_k_compare_version[] = "compare_version";
static const char __pyx_k_python_temp_src[] = "python \"temp\\src\\";
static const char __pyx_k_Failed_to_run_0m[] = " Failed to run.\033[0m";
static const char __pyx_k_python3_temp_src[] = "python3 \"temp\\src\\";
static const char __pyx_k_42_1mCompleted_0m[] = "\033[42;1mCompleted\033[0m                  ";
static const char __pyx_k_FileNotFoundError[] = "FileNotFoundError";
static const char __pyx_k_KeyboardInterrupt[] = "KeyboardInterrupt";
static const char __pyx_k_python_temp_src_2[] = "python \"temp/src/";
static const char __pyx_k_temp_src_output_v[] = "temp\\src\\output.v";
static const char __pyx_k_42_1mFile_saved_to[] = "\033[42;1mFile saved to ";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_python3_temp_src_2[] = "python3 \"temp/src/";
static const char __pyx_k_41_1mDecompiling_0m[] = "\033[41;1mDecompiling...\033[0m";
static const char __pyx_k_ModuleNotFoundError[] = "ModuleNotFoundError";
static const char __pyx_k_from_module_include[] = "      from [module] include *";
static const char __pyx_k_41_1mPlaying_music_0m[] = "\033[41;1mPlaying music.\033[0m";
static const char __pyx_k_42_1mMusic_Started_0m[] = "\033[42;1mMusic Started\033[0m    ";
static const char __pyx_k_Error_Failed_to_build[] = "\nError: Failed to build";
static const char __pyx_k_1m_31mBuild_Stopped_0m[] = "\033[1m\033[31mBuild Stopped\033[0m";
static const char __pyx_k_41_1mINVALID_SYNTAX_0m[] = "\033[41;1mINVALID SYNTAX\033[0m";
static const char __pyx_k_42_1mBuild_Complete_0m[] = "\033[42;1mBuild Complete\033[0m      ";
static const char __pyx_k_File_temp_src_tmp_line[] = "  File \"temp/src/{}.tmp\", line {}";
static const char __pyx_k_No_main_function_found[] = "   No main function found";
static const char __pyx_k_1m_31mStopping_Build_0m[] = "\033[1m\033[31mStopping Build...\033[0m";
static const char __pyx_k_41_1mPlaying_music_0m_2[] = "\033[41;1mPlaying music..\033[0m";
static const char __pyx_k_41_1mPlaying_music_0m_3[] = "\033[41;1mPlaying music...\033[0m";
static const char __pyx_k_Main_function_not_found[] = "Main function not found";
static const char __pyx_k_start_python_m_playsound[] = "start python -m playsound ";
static const char __pyx_k_41_1mAn_error_has_occured[] = "\033[41;1mAn error has occured: ";
static const char __pyx_k_Failed_to_compile_exiting[] = "Failed to compile, exiting...";
static const char __pyx_k_31_1mYOUR_FILE_IS_SAVED_0m[] = "\033[31;1mYOUR FILE IS SAVED!!\033[0m";
static const char __pyx_k_Traceback_Most_Recent_Call[] = "Traceback: Most Recent Call";
static const char __pyx_k_1m_31mDecompile_Canclled_0m[] = "\033[1m\033[31mDecompile Canclled\033[0m";
static const char __pyx_k_42_1mChecking_for_updates_0m[] = "\033[42;1mChecking for updates...\033[0m";
static const char __pyx_k_42_1mDecompiling_Complete_0m[] = "\033[42;1mDecompiling Complete\033[0m";
static const char __pyx_k_31_1m_You_can_t_use_in_include[] = "\033[31;1m You can't use {} in include statement.\033[0m";
static const char __pyx_k_32_1mDo_you_want_to_play_music[] = "\033[32;1mDo you want to play music while compiling? (y/n): \033[0m";
static const char __pyx_k_31_1mDo_you_want_to_run_the_fil[] = "\033[31;1mDo you want to run the file? (y/n) : \033[0m";
static const char __pyx_k_31_1mThe_filename_you_put_was_e[] = "\033[31;1mThe filename you put was either invalid or mismathced, enter file to run : \033[32;1m";
static const char __pyx_k_31_1mWhat_do_you_want_to_call_t[] = "\033[31;1mWhat do you want to call the new file (file will be save to python folder)? : \033[32;1m";
static const char __pyx_k_31_1mYou_did_not_put_a_filename[] = "\033[31;1mYou did not put a filename, enter file to run : \033[32;1m";
static const char __pyx_k_31_1m_Please_update_to_the_late[] = "\033[31;1m  Please update to the latest version\033[0m";
static const char __pyx_k_31_1m_You_can_Ctrl_click_to_ope[] = "\033[31;1m  You can Ctrl+click to open the link in a web browser \033[0m";
static const char __pyx_k_34_1m_https_github_com_Ze7111_V[] = "\033[34;1m  https://github.com/Ze7111/Versace-Programing-language/releases/latest \033[0m";
static const char __pyx_k_41_1mA_newer_version_of_Versace[] = "\033[41;1mA newer version of Versace is available\033[0m";
static const char __pyx_k_41_1mError_Could_not_connect_to[] = "\033[41;1mError: Could not connect to the internet\033[0m";
static const char __pyx_k_41_1mKeyboard_Interrupt_Detecte[] = "\n\033[41;1mKeyboard Interrupt Detected\033[0m";
static const char __pyx_k_41_1mRestart_the_compiler_to_co[] = "\033[41;1mRestart the compiler to continue\033[0m";
static const char __pyx_k_41_1mYou_are_not_allowed_to_imp[] = "\033[41;1mYou are not allowed to import this file\033[0m";
static const char __pyx_k_41_1mYou_are_using_an_unsupport[] = "\033[41;1mYou are using an unsupported version of the compiler, please fix it. The complier will still work but it may not be as stable as the official version.\033[0m";
static const char __pyx_k_41m_30mKeyboard_Interrupt_Detec[] = "\033[41m\033[30mKeyboard Interrupt Detected\033[0m";
static const char __pyx_k_Did_you_mean_to_use_public_main[] = "Did you mean to use \"public main()\"";
static const char __pyx_k_Please_check_the_spelling_and_t[] = "  Please check the spelling and try again.";
static const char __pyx_k_from_rich_import_console_print_c[] = "from rich import console; print = console.Console().print\n";
static const char __pyx_k_https_api_github_com_repos_Ze711[] = "https://api.github.com/repos/Ze7111/Versace-Programing-language/releases/latest";
static const char __pyx_k_41_1mKeyboard_Interrupt_Detecte_2[] = "\033[41;1mKeyboard Interrupt Detected\033[0m";
static PyObject *__pyx_kp_u_;
static PyObject *__pyx_kp_u_0m;
static PyObject *__pyx_kp_u_1m_31mBuild_Stopped_0m;
static PyObject *__pyx_kp_u_1m_31mDecompile_Canclled_0m;
static PyObject *__pyx_kp_u_1m_31mStopping_Build_0m;
static PyObject *__pyx_kp_u_31_1mDo_you_want_to_run_the_fil;
static PyObject *__pyx_kp_u_31_1mThe_filename_you_put_was_e;
static PyObject *__pyx_kp_u_31_1mWhat_do_you_want_to_call_t;
static PyObject *__pyx_kp_u_31_1mYOUR_FILE_IS_SAVED_0m;
static PyObject *__pyx_kp_u_31_1mYou_did_not_put_a_filename;
static PyObject *__pyx_kp_u_31_1m_Please_update_to_the_late;
static PyObject *__pyx_kp_u_31_1m_You_can_Ctrl_click_to_ope;
static PyObject *__pyx_kp_u_31_1m_You_can_t_use_in_include;
static PyObject *__pyx_kp_u_32_1mDo_you_want_to_play_music;
static PyObject *__pyx_kp_u_34_1m_https_github_com_Ze7111_V;
static PyObject *__pyx_kp_u_41_1m;
static PyObject *__pyx_kp_u_41_1mA_newer_version_of_Versace;
static PyObject *__pyx_kp_u_41_1mAn_error_has_occured;
static PyObject *__pyx_kp_u_41_1mBuilding;
static PyObject *__pyx_kp_u_41_1mDecompiling_0m;
static PyObject *__pyx_kp_u_41_1mError_Could_not_connect_to;
static PyObject *__pyx_kp_u_41_1mINVALID_SYNTAX_0m;
static PyObject *__pyx_kp_u_41_1mKeyboard_Interrupt_Detecte;
static PyObject *__pyx_kp_u_41_1mKeyboard_Interrupt_Detecte_2;
static PyObject *__pyx_kp_u_41_1mPlaying_music_0m;
static PyObject *__pyx_kp_u_41_1mPlaying_music_0m_2;
static PyObject *__pyx_kp_u_41_1mPlaying_music_0m_3;
static PyObject *__pyx_kp_u_41_1mRestart_the_compiler_to_co;
static PyObject *__pyx_kp_u_41_1mYou_are_not_allowed_to_imp;
static PyObject *__pyx_kp_u_41_1mYou_are_using_an_unsupport;
static PyObject *__pyx_kp_u_41m_30mError;
static PyObject *__pyx_kp_u_41m_30mKeyboard_Interrupt_Detec;
static PyObject *__pyx_kp_u_42_1mBuild_Complete_0m;
static PyObject *__pyx_kp_u_42_1mChecking_for_updates_0m;
static PyObject *__pyx_kp_u_42_1mCompleted_0m;
static PyObject *__pyx_kp_u_42_1mDecompiling_Complete_0m;
static PyObject *__pyx_kp_u_42_1mFile_saved_to;
static PyObject *__pyx_kp_u_42_1mMusic_Started_0m;
static PyObject *__pyx_kp_u_4_0_0;
static PyObject *__pyx_n_s_C;
static PyObject *__pyx_n_s_C_brace;
static PyObject *__pyx_n_s_C_catch;
static PyObject *__pyx_n_s_C_class;
static PyObject *__pyx_n_s_C_else_if;
static PyObject *__pyx_n_s_C_func;
static PyObject *__pyx_n_s_C_public;
static PyObject *__pyx_kp_u_Did_you_mean_to_use_public_main;
static PyObject *__pyx_kp_u_Error_Failed_to_build;
static PyObject *__pyx_kp_u_Error_Missing;
static PyObject *__pyx_kp_u_Exception;
static PyObject *__pyx_kp_u_FATEL_ERROR;
static PyObject *__pyx_kp_u_Failed_to_compile_exiting;
static PyObject *__pyx_kp_u_Failed_to_run_0m;
static PyObject *__pyx_n_s_FileExistsError;
static PyObject *__pyx_n_s_FileNotFoundError;
static PyObject *__pyx_kp_u_File_temp_src_tmp_line;
static PyObject *__pyx_kp_u_Format_must_be;
static PyObject *__pyx_kp_u_INVALID_MODULE;
static PyObject *__pyx_kp_u_INVALID_SYNTAX;
static PyObject *__pyx_n_s_IO;
static PyObject *__pyx_n_s_IO___init;
static PyObject *__pyx_n_s_IO_error;
static PyObject *__pyx_n_s_IO_inp;
static PyObject *__pyx_n_s_IO_output;
static PyObject *__pyx_n_s_IndexError;
static PyObject *__pyx_n_s_KeyError;
static PyObject *__pyx_n_s_KeyboardInterrupt;
static PyObject *__pyx_kp_u_Main_function_not_found;
static PyObject *__pyx_kp_u_Module;
static PyObject *__pyx_n_s_ModuleNotFoundError;
static PyObject *__pyx_kp_u_No_main_function_found;
static PyObject *__pyx_kp_u_Please_check_the_spelling_and_t;
static PyObject *__pyx_kp_u_Traceback_Most_Recent_Call;
static PyObject *__pyx_n_s_Version;
static PyObject *__pyx_kp_u__12;
static PyObject *__pyx_kp_u__14;
static PyObject *__pyx_kp_u__16;
static PyObject *__pyx_kp_u__17;
static PyObject *__pyx_kp_u__2;
static PyObject *__pyx_kp_u__20;
static PyObject *__pyx_kp_u__21;
static PyObject *__pyx_kp_u__22;
static PyObject *__pyx_kp_u__25;
static PyObject *__pyx_kp_u__26;
static PyObject *__pyx_kp_u__27;
static PyObject *__pyx_kp_u__28;
static PyObject *__pyx_kp_u__29;
static PyObject *__pyx_kp_u__33;
static PyObject *__pyx_kp_u__34;
static PyObject *__pyx_kp_u__35;
static PyObject *__pyx_kp_u__4;
static PyObject *__pyx_kp_u__42;
static PyObject *__pyx_kp_u__43;
static PyObject *__pyx_kp_u__44;
static PyObject *__pyx_kp_u__5;
static PyObject *__pyx_kp_u__50;
static PyObject *__pyx_kp_u__51;
static PyObject *__pyx_kp_u__52;
static PyObject *__pyx_kp_u__53;
static PyObject *__pyx_kp_u__71;
static PyObject *__pyx_n_s_additive;
static PyObject *__pyx_n_s_args;
static PyObject *__pyx_n_s_argv;
static PyObject *__pyx_n_u_black;
static PyObject *__pyx_n_u_blink;
static PyObject *__pyx_n_u_blue;
static PyObject *__pyx_n_u_bold;
static PyObject *__pyx_n_s_brace;
static PyObject *__pyx_n_u_bright_black;
static PyObject *__pyx_n_u_bright_blue;
static PyObject *__pyx_n_u_bright_cyan;
static PyObject *__pyx_n_u_bright_green;
static PyObject *__pyx_n_u_bright_magenta;
static PyObject *__pyx_n_u_bright_red;
static PyObject *__pyx_n_u_bright_white;
static PyObject *__pyx_n_u_bright_yellow;
static PyObject *__pyx_n_s_build;
static PyObject *__pyx_n_u_build;
static PyObject *__pyx_kp_u_build_2;
static PyObject *__pyx_kp_u_build_3;
static PyObject *__pyx_n_s_call;
static PyObject *__pyx_n_s_catch;
static PyObject *__pyx_n_u_catch;
static PyObject *__pyx_n_u_center;
static PyObject *__pyx_n_u_class;
static PyObject *__pyx_n_s_class_2;
static PyObject *__pyx_n_u_clear;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_close;
static PyObject *__pyx_n_u_cls;
static PyObject *__pyx_n_s_code;
static PyObject *__pyx_n_s_colors;
static PyObject *__pyx_n_s_compare_version;
static PyObject *__pyx_n_s_compiler;
static PyObject *__pyx_n_s_create_temp;
static PyObject *__pyx_n_s_current_time;
static PyObject *__pyx_n_u_cyan;
static PyObject *__pyx_kp_u_d;
static PyObject *__pyx_kp_u_d_m_Y_H_M_S;
static PyObject *__pyx_n_s_datatypes;
static PyObject *__pyx_n_s_decomplie;
static PyObject *__pyx_n_u_def;
static PyObject *__pyx_kp_u_def_main;
static PyObject *__pyx_kp_u_def_main_2;
static PyObject *__pyx_n_s_delete_temp;
static PyObject *__pyx_kp_u_dict;
static PyObject *__pyx_n_u_dim;
static PyObject *__pyx_n_s_do_once;
static PyObject *__pyx_n_s_doc;
static PyObject *__pyx_kp_u_does_not_exist;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_u_e;
static PyObject *__pyx_n_u_elif;
static PyObject *__pyx_kp_u_else_if;
static PyObject *__pyx_n_s_else_if_2;
static PyObject *__pyx_kp_u_end;
static PyObject *__pyx_n_s_end_2;
static PyObject *__pyx_n_u_endl;
static PyObject *__pyx_n_s_endswith;
static PyObject *__pyx_n_s_endtypes;
static PyObject *__pyx_n_s_enter;
static PyObject *__pyx_n_s_error;
static PyObject *__pyx_n_u_except;
static PyObject *__pyx_n_s_exists;
static PyObject *__pyx_n_s_exit;
static PyObject *__pyx_n_s_exit_2;
static PyObject *__pyx_n_s_f;
static PyObject *__pyx_n_s_file;
static PyObject *__pyx_n_s_filename;
static PyObject *__pyx_n_s_files;
static PyObject *__pyx_n_s_final;
static PyObject *__pyx_n_u_float;
static PyObject *__pyx_kp_u_float_input;
static PyObject *__pyx_n_s_format;
static PyObject *__pyx_n_s_foundMain;
static PyObject *__pyx_n_u_from;
static PyObject *__pyx_n_s_from_2;
static PyObject *__pyx_kp_u_from_include;
static PyObject *__pyx_kp_u_from_module_include;
static PyObject *__pyx_kp_u_from_rich_import_console_print_c;
static PyObject *__pyx_n_s_func;
static PyObject *__pyx_n_u_func;
static PyObject *__pyx_n_s_get;
static PyObject *__pyx_n_u_green;
static PyObject *__pyx_n_u_hidden;
static PyObject *__pyx_kp_u_https_api_github_com_repos_Ze711;
static PyObject *__pyx_n_s_i;
static PyObject *__pyx_n_u_import;
static PyObject *__pyx_n_s_import_2;
static PyObject *__pyx_n_u_in;
static PyObject *__pyx_n_s_in_module;
static PyObject *__pyx_n_s_inc;
static PyObject *__pyx_n_s_inc__from;
static PyObject *__pyx_n_s_inc_incl;
static PyObject *__pyx_n_s_incl;
static PyObject *__pyx_n_u_include;
static PyObject *__pyx_n_s_index;
static PyObject *__pyx_n_s_init;
static PyObject *__pyx_n_u_innit;
static PyObject *__pyx_n_s_inp;
static PyObject *__pyx_n_s_input;
static PyObject *__pyx_kp_u_input_2;
static PyObject *__pyx_n_u_int;
static PyObject *__pyx_kp_u_int_input;
static PyObject *__pyx_kp_u_int_main;
static PyObject *__pyx_n_s_io;
static PyObject *__pyx_n_u_italic;
static PyObject *__pyx_n_s_json;
static PyObject *__pyx_n_s_justify;
static PyObject *__pyx_n_u_justify;
static PyObject *__pyx_kp_u_justify_2;
static PyObject *__pyx_n_u_left;
static PyObject *__pyx_n_s_lexer;
static PyObject *__pyx_n_s_line;
static PyObject *__pyx_n_s_lines;
static PyObject *__pyx_kp_u_list;
static PyObject *__pyx_n_s_listdir;
static PyObject *__pyx_n_s_localtime;
static PyObject *__pyx_n_s_lower;
static PyObject *__pyx_kp_u_m;
static PyObject *__pyx_n_u_magenta;
static PyObject *__pyx_kp_u_main;
static PyObject *__pyx_n_s_main_2;
static PyObject *__pyx_n_s_main_3;
static PyObject *__pyx_n_u_main_3;
static PyObject *__pyx_n_s_metaclass;
static PyObject *__pyx_n_s_mkdir;
static PyObject *__pyx_n_s_module;
static PyObject *__pyx_n_s_module_2;
static PyObject *__pyx_n_s_module_path;
static PyObject *__pyx_kp_u_music_mp3;
static PyObject *__pyx_n_s_music_option;
static PyObject *__pyx_n_s_music_path;
static PyObject *__pyx_kp_u_n;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_name_2;
static PyObject *__pyx_n_s_new_final;
static PyObject *__pyx_n_u_newl;
static PyObject *__pyx_n_s_newlines;
static PyObject *__pyx_n_u_nt;
static PyObject *__pyx_n_s_numtabs;
static PyObject *__pyx_n_s_open;
static PyObject *__pyx_n_s_org_final;
static PyObject *__pyx_n_s_os;
static PyObject *__pyx_n_u_out;
static PyObject *__pyx_n_s_output;
static PyObject *__pyx_n_s_parse;
static PyObject *__pyx_n_s_path;
static PyObject *__pyx_kp_u_pip_install;
static PyObject *__pyx_n_s_playsound;
static PyObject *__pyx_n_s_prepare;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_kp_u_print_2;
static PyObject *__pyx_kp_u_print_3;
static PyObject *__pyx_n_s_public;
static PyObject *__pyx_n_u_public;
static PyObject *__pyx_kp_u_py;
static PyObject *__pyx_n_s_py_code;
static PyObject *__pyx_kp_u_python3_temp_src;
static PyObject *__pyx_kp_u_python3_temp_src_2;
static PyObject *__pyx_kp_u_python_temp_src;
static PyObject *__pyx_kp_u_python_temp_src_2;
static PyObject *__pyx_n_s_qualname;
static PyObject *__pyx_n_u_r;
static PyObject *__pyx_kp_u_r_2;
static PyObject *__pyx_n_s_range;
static PyObject *__pyx_n_s_readlines;
static PyObject *__pyx_n_u_red;
static PyObject *__pyx_n_s_remove;
static PyObject *__pyx_n_s_replace;
static PyObject *__pyx_n_u_repr;
static PyObject *__pyx_n_s_requests;
static PyObject *__pyx_n_s_response;
static PyObject *__pyx_n_u_return;
static PyObject *__pyx_n_u_reverse;
static PyObject *__pyx_n_s_rich;
static PyObject *__pyx_n_u_right;
static PyObject *__pyx_n_s_rmtree;
static PyObject *__pyx_n_s_rstrip;
static PyObject *__pyx_n_u_rw;
static PyObject *__pyx_n_s_self;
static PyObject *__pyx_n_s_shell;
static PyObject *__pyx_n_s_shutil;
static PyObject *__pyx_n_s_sleep;
static PyObject *__pyx_n_s_sort;
static PyObject *__pyx_n_u_space;
static PyObject *__pyx_n_s_split;
static PyObject *__pyx_kp_u_start_python_m_playsound;
static PyObject *__pyx_n_s_starter;
static PyObject *__pyx_n_s_startswith;
static PyObject *__pyx_n_s_statement;
static PyObject *__pyx_n_s_statements;
static PyObject *__pyx_n_s_status_code;
static PyObject *__pyx_n_u_str;
static PyObject *__pyx_kp_u_str_input;
static PyObject *__pyx_n_s_strftime;
static PyObject *__pyx_n_s_strip;
static PyObject *__pyx_kp_u_style;
static PyObject *__pyx_n_s_styles;
static PyObject *__pyx_n_s_subprocess;
static PyObject *__pyx_n_s_symobol;
static PyObject *__pyx_n_s_sys;
static PyObject *__pyx_n_s_system;
static PyObject *__pyx_kp_u_t;
static PyObject *__pyx_n_s_tab;
static PyObject *__pyx_n_u_tab;
static PyObject *__pyx_n_s_tabs;
static PyObject *__pyx_n_u_tag_name;
static PyObject *__pyx_n_u_temp;
static PyObject *__pyx_kp_u_temp_src;
static PyObject *__pyx_kp_u_temp_src_2;
static PyObject *__pyx_kp_u_temp_src_3;
static PyObject *__pyx_kp_u_temp_src_4;
static PyObject *__pyx_kp_u_temp_src_output_v;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_s_text;
static PyObject *__pyx_n_s_time;
static PyObject *__pyx_kp_u_tmp;
static PyObject *__pyx_kp_u_tmp_2;
static PyObject *__pyx_n_u_underline;
static PyObject *__pyx_kp_u_v;
static PyObject *__pyx_n_s_var;
static PyObject *__pyx_n_s_versace;
static PyObject *__pyx_kp_s_versace_pyx;
static PyObject *__pyx_n_u_w;
static PyObject *__pyx_n_u_white;
static PyObject *__pyx_n_s_write;
static PyObject *__pyx_n_u_y;
static PyObject *__pyx_n_u_yellow;
static PyObject *__pyx_pf_7versace_1C_class_(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_line, PyObject *__pyx_v_numtabs); /* proto */
static PyObject *__pyx_pf_7versace_1C_2else_if(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_line, PyObject *__pyx_v_numtabs); /* proto */
static PyObject *__pyx_pf_7versace_1C_4public(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_line, PyObject *__pyx_v_numtabs); /* proto */
static PyObject *__pyx_pf_7versace_1C_6func(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_line, PyObject *__pyx_v_numtabs); /* proto */
static PyObject *__pyx_pf_7versace_1C_8catch(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_line, PyObject *__pyx_v_numtabs); /* proto */
static PyObject *__pyx_pf_7versace_1C_10brace(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_line, PyObject *__pyx_v_numtabs); /* proto */
static PyObject *__pyx_pf_7versace_3inc_incl(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_line); /* proto */
static PyObject *__pyx_pf_7versace_3inc_2_from(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_line, CYTHON_UNUSED PyObject *__pyx_v_tabs, PyObject *__pyx_v_final); /* proto */
static PyObject *__pyx_pf_7versace_2IO___init__(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self); /* proto */
static PyObject *__pyx_pf_7versace_2IO_2output(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text); /* proto */
static PyObject *__pyx_pf_7versace_2IO_4inp(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_self, PyObject *__pyx_v_text, PyObject *__pyx_v_tabs); /* proto */
static PyObject *__pyx_pf_7versace_2IO_6error(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_text); /* proto */
static PyObject *__pyx_pf_7versace_compiler(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_final, PyObject *__pyx_v_decomplie, PyObject *__pyx_v_filename); /* proto */
static PyObject *__pyx_pf_7versace_2lexer(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_lines, PyObject *__pyx_v_filename, PyObject *__pyx_v_decomplie); /* proto */
static PyObject *__pyx_pf_7versace_4main(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_filename, PyObject *__pyx_v_decomplie); /* proto */
static PyObject *__pyx_pf_7versace_6build(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_filename, PyObject *__pyx_v_music_option, PyObject *__pyx_v_Version, PyObject *__pyx_v_music_path, CYTHON_UNUSED PyObject *__pyx_v_args); /* proto */
static PyObject *__pyx_pf_7versace_8starter(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_filename, PyObject *__pyx_v_music_option, PyObject *__pyx_v_Version, PyObject *__pyx_v_music_path, PyObject *__pyx_v_argv); /* proto */
static PyObject *__pyx_pf_7versace_10create_temp(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_7versace_12delete_temp(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static __Pyx_CachedCFunction __pyx_umethod_PyUnicode_Type_rstrip = {0, &__pyx_n_s_rstrip, 0, 0, 0};
static PyObject *__pyx_float_0_5;
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_1;
static PyObject *__pyx_int_2;
static PyObject *__pyx_int_4;
static PyObject *__pyx_int_5;
static PyObject *__pyx_int_200;
static PyObject *__pyx_int_neg_1;
static PyObject *__pyx_int_neg_10;
static PyObject *__pyx_tuple__3;
static PyObject *__pyx_tuple__6;
static PyObject *__pyx_tuple__7;
static PyObject *__pyx_tuple__8;
static PyObject *__pyx_tuple__9;
static PyObject *__pyx_slice__40;
static PyObject *__pyx_slice__45;
static PyObject *__pyx_tuple__10;
static PyObject *__pyx_tuple__11;
static PyObject *__pyx_tuple__13;
static PyObject *__pyx_tuple__15;
static PyObject *__pyx_tuple__18;
static PyObject *__pyx_tuple__19;
static PyObject *__pyx_tuple__23;
static PyObject *__pyx_tuple__24;
static PyObject *__pyx_tuple__30;
static PyObject *__pyx_tuple__31;
static PyObject *__pyx_tuple__32;
static PyObject *__pyx_tuple__36;
static PyObject *__pyx_tuple__37;
static PyObject *__pyx_tuple__38;
static PyObject *__pyx_tuple__39;
static PyObject *__pyx_tuple__41;
static PyObject *__pyx_tuple__46;
static PyObject *__pyx_tuple__47;
static PyObject *__pyx_tuple__48;
static PyObject *__pyx_tuple__49;
static PyObject *__pyx_tuple__54;
static PyObject *__pyx_tuple__55;
static PyObject *__pyx_tuple__56;
static PyObject *__pyx_tuple__57;
static PyObject *__pyx_tuple__58;
static PyObject *__pyx_tuple__59;
static PyObject *__pyx_tuple__60;
static PyObject *__pyx_tuple__61;
static PyObject *__pyx_tuple__62;
static PyObject *__pyx_tuple__63;
static PyObject *__pyx_tuple__64;
static PyObject *__pyx_tuple__65;
static PyObject *__pyx_tuple__66;
static PyObject *__pyx_tuple__67;
static PyObject *__pyx_tuple__68;
static PyObject *__pyx_tuple__69;
static PyObject *__pyx_tuple__70;
static PyObject *__pyx_tuple__72;
static PyObject *__pyx_tuple__73;
static PyObject *__pyx_tuple__75;
static PyObject *__pyx_tuple__77;
static PyObject *__pyx_tuple__79;
static PyObject *__pyx_tuple__81;
static PyObject *__pyx_tuple__83;
static PyObject *__pyx_tuple__85;
static PyObject *__pyx_tuple__87;
static PyObject *__pyx_tuple__89;
static PyObject *__pyx_tuple__91;
static PyObject *__pyx_tuple__93;
static PyObject *__pyx_tuple__95;
static PyObject *__pyx_tuple__97;
static PyObject *__pyx_tuple__99;
static PyObject *__pyx_tuple__101;
static PyObject *__pyx_tuple__103;
static PyObject *__pyx_tuple__105;
static PyObject *__pyx_tuple__107;
static PyObject *__pyx_tuple__108;
static PyObject *__pyx_tuple__111;
static PyObject *__pyx_codeobj__74;
static PyObject *__pyx_codeobj__76;
static PyObject *__pyx_codeobj__78;
static PyObject *__pyx_codeobj__80;
static PyObject *__pyx_codeobj__82;
static PyObject *__pyx_codeobj__84;
static PyObject *__pyx_codeobj__86;
static PyObject *__pyx_codeobj__88;
static PyObject *__pyx_codeobj__90;
static PyObject *__pyx_codeobj__92;
static PyObject *__pyx_codeobj__94;
static PyObject *__pyx_codeobj__96;
static PyObject *__pyx_codeobj__98;
static PyObject *__pyx_codeobj__100;
static PyObject *__pyx_codeobj__102;
static PyObject *__pyx_codeobj__104;
static PyObject *__pyx_codeobj__106;
static PyObject *__pyx_codeobj__109;
static PyObject *__pyx_codeobj__110;