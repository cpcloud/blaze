Usage Modes
===========

This documents explains the key differences between interactive use of blaze
and more abstract use of blaze.

Interactive Use
===============

To summarize :doc:`interactivity`, blaze lets you combine both a *resource*
**and** an *expression* to let you see the results of your computations
immediately. For example,

    .. code-block:: python

       >>> from blaze import Data
       >>> d = Data('sqlite:///tpc.db')
       >>> d
       Data:       Engine(sqlite:///tpc.db)
       DataShape:  {
         customer: var * {
           id: int32,
           name: string[25],
           address: string[40],
           nation_id: map[int64, {
             id: int32,
         ...

       >>> d.fields
       ['customer',
        'lineitem',
        'nation',
        'orders',
        'part',
        'partsupp',
        'region',
        'supplier']

       >>> d.customer.fields
       ['id',
        'name',
        'address',
        'nation_id',
        'phone',
        'account_balance',
        'market_segment',
        'comment']

       >>> d.customer.market_segment.count_values()
         market_segment  count
       0     HOUSEHOLD   30189
       1     BUILDING    30142
       2     FURNITURE   29968
       3     MACHINERY   29949
       4     AUTOMOBILE  29752


The way this works is that :func:`~blaze.interactive.Data` is actually a
function that generates an instance of a class called
:class:`~blaze.interactive.InteractiveSymbol`. Instances of
:class:`~blaze.interactive.InteractiveSymbol` work the same way as
:class:`~blaze.expr.expressions.Symbol` instances except that
``InteractiveSymbol`` instances are bound to a *resource*. To make these
objects feel interactive, :class:`~blaze.interactive.InteractiveSymbol` class
implements the ``__repr__`` method differently than
:class:`~blaze.expr.expressions.Symbol` instances. Its ``__repr__`` method
calls :func:`~blaze.compute.core.compute`, then converts the result of that
call into a concrete object such as a pandas DataFrame, ``int``, pandas Series,
etc and then calls ``__repr__`` on that concrete object. This makes it seamless
to interact in a pandas-like way with systems that are typically quite
cumbersome or clunky to interact with in Python, such as SQL databases.

   .. note::

      Always remember that any computation with an ``InteractiveSymbol`` will
      *return a blaze expression*. Even if you do something like

         .. code-block:: python

            r = t.price.sum()

      ``r`` is still an instance of :class:`~blaze.expr.expressions.Expr`.

Abstract Usage
==============

Alternatively, one can live completely divorced from an actual data source and
build up an expression without knowledge of what backend we're executing
against.
