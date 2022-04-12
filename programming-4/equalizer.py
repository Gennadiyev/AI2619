import numpy as np

class Equalizer():

    class EqualizerNode():
        def __init__(self, all_freq, node_freq, gain, range=0.1, nodetype="gain"):
            self.all_freq = all_freq
            self.freq = node_freq
            self.gain = gain
            self.range = range
            assert(nodetype in ["gain", "lowcut", "highcut"])
            self.type = nodetype
            self.hash = hash(np.random.random())
        def __repr__(self):
            if self.type == "gain":
                return f"<EqualizerNode.gain freq={self.freq}Hz, gain={self.gain}, range={self.range}>"
            elif self.type == "lowcut":
                return f"<EqualizerNode.lowcut freq={self.freq}Hz>"
            elif self.type == "highcut":
                return f"<EqualizerNode.highcut freq={self.freq}Hz>"
            else:
                return f"<EqualizerNode type=unknown>"
        def __str__(self):
            return self.__repr__()
        def __hash__(self):
            return self.hash
        def generate_array(self):
            effect = []
            if self.type == "gain":
                for i in range(len(self.all_freq)):
                    this_freq = self.all_freq[i]
                    if this_freq >= self.freq * (1 - self.range) and this_freq <= self.freq * (1 + self.range):
                        gain_strength = 1 - abs(self.freq - this_freq) / (self.range * self.freq)
                        gain_ratio = (np.sin(-np.pi * 0.5 + np.pi * gain_strength) + 1) * 0.5
                        effect.append(1 + self.gain * gain_ratio)
                    else:
                        effect.append(1)
            elif self.type == "lowcut":
                for i in range(len(self.all_freq)):
                    this_freq = self.all_freq[i]
                    if this_freq < self.freq:
                        effect.append(0)
                    else:
                        effect.append(1)
            elif self.type == "highcut":
                for i in range(len(self.all_freq)):
                    this_freq = self.all_freq[i]
                    if this_freq > self.freq:
                        effect.append(0)
                    else:
                        effect.append(1)
            else:
                raise ValueError("Unknown node type")
            return effect
    
    def __init__(self, freq, name):
        self.freq = freq
        self.name = name
        self.nodes = []

    def get_effect(self):
        effect = []
        for i in range(len(self.nodes)):
            effect.append(self.nodes[i].generate_array())
        # Sum all the effects
        effect = np.prod(effect, axis=0)
        return effect
    
    def get_nodes(self):
        return self.nodes

    def add_node(self, nodetype, freq, gain=None, range=0.1):
        if nodetype == "gain":
            self.nodes.append(Equalizer.EqualizerNode(self.freq, freq, gain, range, nodetype))
        elif nodetype == "lowcut":
            for node in self.nodes:
                if node.type == "lowcut":
                    raise ValueError("Lowcut node already exists")
            self.nodes.append(Equalizer.EqualizerNode(self.freq, freq, gain, range, nodetype))
        elif nodetype == "highcut":
            for node in self.nodes:
                if node.type == "highcut":
                    raise ValueError("Highcut node already exists")
            self.nodes.append(Equalizer.EqualizerNode(self.freq, freq, gain, range, nodetype))
        else:
            raise ValueError("Node type must be 'gain', 'lowcut', or 'highcut'")

    def get_gain(self, freq):
        effect = self.get_effect()
        # Find the closest frequency
        closest_freq = self.freq[np.argmin(np.abs(self.freq - freq))]
        # Find the index of the closest frequency
        closest_freq_index = closest_freq.index(freq)
        # Return the gain at that index
        return effect[closest_freq_index]
        
    def plot_show(self):
        import matplotlib.pyplot as plt
        effect = self.get_effect()
        plt.figure(figsize=(10,6))
        plt.plot(self.freq, effect)
        plt.xlabel(r'Frequency')
        plt.xlim(min(self.freq), max(self.freq))
        plt.ylabel(r'Gain')
        plt.title(f"{self.name} - Equalizer Effect")
        plt.show()
    
    def apply_effect(self, source_arr_f, source_arr_t, source_arr_zxx):
        effect = self.get_effect()
        # Apply the effect to the source array
        import copy
        zxx = copy.deepcopy(source_arr_zxx)
        for i in range(len(source_arr_t)):
            zxx[:, i] = zxx[:, i] * effect
        return source_arr_f, source_arr_t, zxx
