ARG BASE_IMAGE_TAG=v0.44.1
FROM ghcr.io/pyvista/pyvista:$BASE_IMAGE_TAG

COPY --chown=${NB_UID}:${NB_GID} mamba.txt /tmp/
RUN mamba install --yes --file /tmp/mamba.txt && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

RUN pip install --no-cache-dir --index-url https://gmsh.info/python-packages-dev-nox \
    --pre "gmsh>=4.11" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

COPY --chown=${NB_UID}:${NB_GID} requirements-no-deps.txt /tmp/
RUN pip install --no-deps --no-cache-dir --requirement /tmp/requirements-no-deps.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

COPY --chown=${NB_UID}:${NB_GID} . ${HOME}
WORKDIR ${HOME}
