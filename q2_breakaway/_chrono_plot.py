import qiime2
from q2_types.sample_data import AlphaDiversityFormat


def chrono_plot(output_dir: str, alpha_diversity: AlphaDiversityFormat,
        metadata: qiime2.CategoricalMetadataColumn):
    # Parse sample dates specified in the metadata column: use datetime x axis
    # (see e.g.
    # https://docs.bokeh.org/en/latest/docs/user_guide/plotting.html#datetime-axes)
    #
    # color samples/error bars by method name or model type? (this is info in alpha_diversity)
    #
    # add Bokeh dependency
    pass
