# ex: set ro:
# DO NOT EDIT.
# generated by smc (http://smc.sourceforge.net/)
# from file : subscription.sm

import satori.rtm.generated.statemap as statemap


class SubscriptionState(statemap.State):

    def Entry(self, fsm):
        pass

    def Exit(self, fsm):
        pass

    def ChannelError(self, fsm, error):
        self.Default(fsm)

    def Connect(self, fsm):
        self.Default(fsm)

    def Disconnect(self, fsm):
        self.Default(fsm)

    def ModeChange(self, fsm):
        self.Default(fsm)

    def SubscribeError(self, fsm):
        self.Default(fsm)

    def SubscribeOK(self, fsm):
        self.Default(fsm)

    def UnsubscribeAttempt(self, fsm):
        self.Default(fsm)

    def UnsubscribeError(self, fsm):
        self.Default(fsm)

    def UnsubscribeOK(self, fsm):
        self.Default(fsm)

    def Default(self, fsm):
        msg = "\n\tState: %s\n\tTransition: %s" % (
            fsm.getState().getName(), fsm.getTransition())
        raise statemap.TransitionUndefinedException(msg)

class Subscription_Default(SubscriptionState):
    pass

class Subscription_Unsubscribed(Subscription_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.on_enter_unsubscribed()
        ctxt._change_mode_from_cycle_to_linked()

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.on_leave_unsubscribed()

    def ChannelError(self, fsm, error):
        # No actions.
        pass

    def Connect(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt._is_mode_not_unlinked() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Subscription.Subscribing)
            fsm.getState().Entry(fsm)
        else:
            # No actions.
            pass


    def Disconnect(self, fsm):
        # No actions.
        pass

    def ModeChange(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt._is_ready_to_subscribe() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Subscription.Subscribing)
            fsm.getState().Entry(fsm)
        else:
            # No actions.
            pass


    def SubscribeError(self, fsm):
        # No actions.
        pass

    def SubscribeOK(self, fsm):
        # No actions.
        pass

    def UnsubscribeAttempt(self, fsm):
        # No actions.
        pass

    def UnsubscribeError(self, fsm):
        # No actions.
        pass

    def UnsubscribeOK(self, fsm):
        # No actions.
        pass

class Subscription_Subscribed(Subscription_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.on_enter_subscribed()

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.on_leave_subscribed()

    def ChannelError(self, fsm, error):
        ctxt = fsm.getOwner()
        if ctxt._is_fatal_channel_error(error) :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt._set_last_error(error)
            finally:
                fsm.setState(Subscription.Failed)
                fsm.getState().Entry(fsm)
        elif ctxt._retire_position_if_necessary(error) :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt._set_last_error(error)
            finally:
                fsm.setState(Subscription.Subscribing)
                fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt._set_last_error(error)
            finally:
                fsm.setState(Subscription.Subscribing)
                fsm.getState().Entry(fsm)


    def Connect(self, fsm):
        # No actions.
        pass

    def Disconnect(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Unsubscribed)
        fsm.getState().Entry(fsm)

    def ModeChange(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt._is_mode_not_linked() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Subscription.Unsubscribing)
            fsm.getState().Entry(fsm)
        else:
            # No actions.
            pass


    def SubscribeError(self, fsm):
        # No actions.
        pass

    def SubscribeOK(self, fsm):
        # No actions.
        pass

    def UnsubscribeAttempt(self, fsm):
        # No actions.
        pass

    def UnsubscribeError(self, fsm):
        # No actions.
        pass

    def UnsubscribeOK(self, fsm):
        # No actions.
        pass

class Subscription_Subscribing(Subscription_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt._send_subscribe_request()
        ctxt.on_enter_subscribing()

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.on_leave_subscribing()

    def ChannelError(self, fsm, error):
        # No actions.
        pass

    def Connect(self, fsm):
        # No actions.
        pass

    def Disconnect(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Unsubscribed)
        fsm.getState().Entry(fsm)

    def ModeChange(self, fsm):
        # No actions.
        pass

    def SubscribeError(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt._is_mode_linked() :
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt._set_last_error('Subscribe error')
            finally:
                fsm.setState(Subscription.Failed)
                fsm.getState().Entry(fsm)
        elif ctxt._is_mode_unlinked() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Subscription.Unsubscribed)
            fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            fsm.clearState()
            try:
                ctxt._change_mode_from_cycle_to_linked()
            finally:
                fsm.setState(Subscription.Subscribing)
                fsm.getState().Entry(fsm)


    def SubscribeOK(self, fsm):
        ctxt = fsm.getOwner()
        if ctxt._is_mode_linked() :
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Subscription.Subscribed)
            fsm.getState().Entry(fsm)
        else:
            fsm.getState().Exit(fsm)
            # No actions.
            pass
            fsm.setState(Subscription.Unsubscribing)
            fsm.getState().Entry(fsm)


    def UnsubscribeAttempt(self, fsm):
        # No actions.
        pass

    def UnsubscribeError(self, fsm):
        # No actions.
        pass

    def UnsubscribeOK(self, fsm):
        # No actions.
        pass

class Subscription_Unsubscribing(Subscription_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt._send_unsubscribe_request()
        ctxt.on_enter_unsubscribing()

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.on_leave_unsubscribing()

    def ChannelError(self, fsm, error):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Unsubscribed)
        fsm.getState().Entry(fsm)

    def Connect(self, fsm):
        # No actions.
        pass

    def Disconnect(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Unsubscribed)
        fsm.getState().Entry(fsm)

    def ModeChange(self, fsm):
        # No actions.
        pass

    def SubscribeError(self, fsm):
        # No actions.
        pass

    def SubscribeOK(self, fsm):
        # No actions.
        pass

    def UnsubscribeAttempt(self, fsm):
        # No actions.
        pass

    def UnsubscribeError(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Subscribed)
        fsm.getState().Entry(fsm)

    def UnsubscribeOK(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Unsubscribed)
        fsm.getState().Entry(fsm)

class Subscription_Failed(Subscription_Default):

    def Entry(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.on_enter_failed(ctxt._last_error)

    def Exit(self, fsm):
        ctxt = fsm.getOwner()
        ctxt.on_leave_failed()

    def ChannelError(self, fsm, error):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Unsubscribed)
        fsm.getState().Entry(fsm)

    def Connect(self, fsm):
        # No actions.
        pass

    def Disconnect(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Unsubscribed)
        fsm.getState().Entry(fsm)

    def ModeChange(self, fsm):
        # No actions.
        pass

    def SubscribeError(self, fsm):
        # No actions.
        pass

    def SubscribeOK(self, fsm):
        # No actions.
        pass

    def UnsubscribeAttempt(self, fsm):
        # No actions.
        pass

    def UnsubscribeError(self, fsm):
        # No actions.
        pass

    def UnsubscribeOK(self, fsm):
        fsm.getState().Exit(fsm)
        fsm.setState(Subscription.Unsubscribed)
        fsm.getState().Entry(fsm)

class Subscription(object):

    Unsubscribed = Subscription_Unsubscribed('Subscription.Unsubscribed', 0)
    Subscribed = Subscription_Subscribed('Subscription.Subscribed', 1)
    Subscribing = Subscription_Subscribing('Subscription.Subscribing', 2)
    Unsubscribing = Subscription_Unsubscribing('Subscription.Unsubscribing', 3)
    Failed = Subscription_Failed('Subscription.Failed', 4)
    Default = Subscription_Default('Subscription.Default', -1)

class Subscription_sm(statemap.FSMContext):

    def __init__(self, owner):
        statemap.FSMContext.__init__(self, Subscription.Unsubscribed)
        self._owner = owner

    def __getattr__(self, attrib):
        def trans_sm(*arglist):
            self._transition = attrib
            getattr(self.getState(), attrib)(self, *arglist)
            self._transition = None
        return trans_sm

    def enterStartState(self):
        self._state.Entry(self)

    def getOwner(self):
        return self._owner

# Local variables:
#  buffer-read-only: t
# End:
